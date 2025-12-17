/**
 * Infrastructure: PrismaStudentRepository
 * 
 * Implementación concreta del repositorio usando Prisma ORM.
 * Adaptador entre el dominio y la base de datos (Adapter Pattern).
 * 
 * @infrastructure Prisma + PostgreSQL
 */

import { PrismaClient, Student as PrismaStudent } from '@prisma/client';
import {
  IStudentRepository,
  StudentFilters,
  PaginationOptions,
  PaginatedResult,
} from '@/domain/repositories/IStudentRepository';
import { Student, StudentProps, AcademicModel } from '@/domain/entities/Student';
import { Score } from '@/domain/value-objects/Score';

/**
 * Implementación del repositorio con Prisma
 */
export class PrismaStudentRepository implements IStudentRepository {
  constructor(private readonly prisma: PrismaClient) {}

  /**
   * Buscar por ID
   */
  public async findById(id: string): Promise<Student | null> {
    const prismaStudent = await this.prisma.student.findUnique({
      where: { id },
    });

    return prismaStudent ? this.toDomain(prismaStudent) : null;
  }

  /**
   * Buscar por documento
   */
  public async findByDocument(documentNumber: string): Promise<Student | null> {
    const prismaStudent = await this.prisma.student.findFirst({
      where: { numeroDocumento: documentNumber },
      orderBy: { anio: 'desc' }, // Más reciente primero
    });

    return prismaStudent ? this.toDomain(prismaStudent) : null;
  }

  /**
   * Listar todos con filtros
   */
  public async findAll(filters?: StudentFilters): Promise<Student[]> {
    const where = this.buildWhereClause(filters);

    const prismaStudents = await this.prisma.student.findMany({
      where,
      orderBy: { puntajeGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Listar con paginación
   */
  public async findAllPaginated(
    filters?: StudentFilters,
    pagination: PaginationOptions = { page: 1, pageSize: 10 }
  ): Promise<PaginatedResult<Student>> {
    const where = this.buildWhereClause(filters);
    const skip = (pagination.page - 1) * pagination.pageSize;

    const [prismaStudents, total] = await Promise.all([
      this.prisma.student.findMany({
        where,
        skip,
        take: pagination.pageSize,
        orderBy: { puntajeGlobal: 'desc' },
      }),
      this.prisma.student.count({ where }),
    ]);

    return {
      data: prismaStudents.map((ps) => this.toDomain(ps)),
      total,
      page: pagination.page,
      pageSize: pagination.pageSize,
      totalPages: Math.ceil(total / pagination.pageSize),
    };
  }

  /**
   * Buscar por año y período
   */
  public async findByYearAndPeriod(year: number, period: number): Promise<Student[]> {
    const prismaStudents = await this.prisma.student.findMany({
      where: { anio: year },
      orderBy: { puntajeGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Buscar por grado
   */
  public async findByGrade(grade: number, year: number, period: number): Promise<Student[]> {
    const prismaStudents = await this.prisma.student.findMany({
      where: { grupo: grade.toString(), anio: year },
      orderBy: { puntajeGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Buscar por modelo
   */
  public async findByModel(
    model: AcademicModel,
    year: number,
    period: number
  ): Promise<Student[]> {
    const modeloStr = model === AcademicModel.REGULAR ? 'Regular' : 'Flexible';
    const prismaStudents = await this.prisma.student.findMany({
      where: {
        modelo: modeloStr,
        anio: year,
      },
      orderBy: { puntajeGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Buscar estudiantes destacados (puntaje >= 267 = Avanzado)
   */
  public async findHighPerformers(year: number, period: number): Promise<Student[]> {
    const prismaStudents = await this.prisma.student.findMany({
      where: {
        anio: year,
        puntajeGlobal: { gte: 267 }, // Umbral nivel Avanzado
      },
      orderBy: { puntajeGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Guardar estudiante
   */
  public async save(student: Student): Promise<Student> {
    const data = this.toPrisma(student);

    const prismaStudent = await this.prisma.student.upsert({
      where: { id: student.getId() },
      update: data,
      create: { ...data, id: student.getId() },
    });

    return this.toDomain(prismaStudent);
  }

  /**
   * Guardar múltiples (bulk)
   */
  public async saveMany(students: Student[]): Promise<Student[]> {
    // Usar transacción para atomicidad
    const results = await this.prisma.$transaction(
      students.map((student) =>
        this.prisma.student.upsert({
          where: { id: student.getId() },
          update: this.toPrisma(student),
          create: { ...this.toPrisma(student), id: student.getId() },
        })
      )
    );

    return results.map((ps) => this.toDomain(ps));
  }

  /**
   * Eliminar
   */
  public async delete(id: string): Promise<void> {
    await this.prisma.student.delete({ where: { id } });
  }

  /**
   * Contar con filtros
   */
  public async count(filters?: StudentFilters): Promise<number> {
    const where = this.buildWhereClause(filters);
    return this.prisma.student.count({ where });
  }

  /**
   * Verificar existencia
   */
  public async exists(id: string): Promise<boolean> {
    const count = await this.prisma.student.count({ where: { id } });
    return count > 0;
  }

  // ========== MAPPERS ==========

  /**
   * Convertir de Prisma a Dominio
   */
  private toDomain(prismaStudent: PrismaStudent): Student {
    // Construir nombre completo
    const fullName = [
      prismaStudent.primerNombre,
      prismaStudent.segundoNombre,
      prismaStudent.primerApellido,
      prismaStudent.segundoApellido,
    ]
      .filter(Boolean)
      .join(' ');

    // Convertir modelo a enum
    const model =
      prismaStudent.modelo === 'Regular' ? AcademicModel.REGULAR : AcademicModel.FLEXIBLE;

    // Extraer grado del grupo (11A -> 11, P3A -> 3)
    const gradeMatch = prismaStudent.grupo.match(/\d+/);
    const grade = gradeMatch ? parseInt(gradeMatch[0]) : 11;

    const props: StudentProps = {
      id: prismaStudent.id,
      documentNumber: prismaStudent.numeroDocumento,
      fullName,
      grade,
      model,
      year: prismaStudent.anio,
      period: 1, // Por defecto período 1
      scores: {
        reading: Score.create(prismaStudent.lecturaCritica),
        mathematics: Score.create(prismaStudent.matematicas),
        socialSciences: Score.create(prismaStudent.socialesCiudadanas),
        naturalSciences: Score.create(prismaStudent.cienciasNaturales),
        english: Score.create(prismaStudent.ingles),
        global: Score.create(prismaStudent.puntajeGlobal),
      },
    };

    return Student.create(props);
  }

  /**
   * Convertir de Dominio a Prisma
   */
  private toPrisma(student: Student): Omit<PrismaStudent, 'id' | 'createdAt' | 'updatedAt'> {
    const scores = student.getScores();
    const fullName = student.getFullName();
    const nameParts = fullName.split(' ');

    // Intentar extraer nombres y apellidos
    const primerNombre = nameParts[0] || '';
    const segundoNombre = nameParts.length > 3 ? nameParts[1] : '';
    const primerApellido = nameParts.length > 3 ? nameParts[2] : nameParts[1] || '';
    const segundoApellido = nameParts.length > 3 ? nameParts[3] : nameParts[2] || '';

    return {
      primerApellido,
      segundoApellido,
      primerNombre,
      segundoNombre,
      tipoDocumento: 'TI', // Por defecto
      numeroDocumento: student.getDocumentNumber(),
      grupo: `${student.getGrade()}A`, // Por defecto
      modelo: student.getModel() === AcademicModel.REGULAR ? 'Regular' : 'Flexible',
      anio: student.getYear(),
      lecturaCritica: Math.round(scores.reading.getValue()),
      matematicas: Math.round(scores.mathematics.getValue()),
      socialesCiudadanas: Math.round(scores.socialSciences.getValue()),
      cienciasNaturales: Math.round(scores.naturalSciences.getValue()),
      ingles: Math.round(scores.english.getValue()),
      puntajeGlobal: Math.round(scores.global.getValue()),
    };
  }

  /**
   * Construir cláusula WHERE desde filtros
   */
  private buildWhereClause(filters?: StudentFilters): any {
    if (!filters) return {};

    const modeloStr = filters.model
      ? filters.model === AcademicModel.REGULAR
        ? 'Regular'
        : 'Flexible'
      : undefined;

    return {
      ...(filters.year && { anio: filters.year }),
      ...(filters.grade && { grupo: { contains: filters.grade.toString() } }),
      ...(modeloStr && { modelo: modeloStr }),
      ...(filters.minGlobalScore && { puntajeGlobal: { gte: filters.minGlobalScore } }),
      ...(filters.maxGlobalScore && { puntajeGlobal: { lte: filters.maxGlobalScore } }),
    };
  }
}

