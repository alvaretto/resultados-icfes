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
      where: { documentNumber },
      orderBy: { year: 'desc' }, // Más reciente primero
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
      orderBy: { scoreGlobal: 'desc' },
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
        orderBy: { scoreGlobal: 'desc' },
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
      where: { year, period },
      orderBy: { scoreGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Buscar por grado
   */
  public async findByGrade(grade: number, year: number, period: number): Promise<Student[]> {
    const prismaStudents = await this.prisma.student.findMany({
      where: { grade, year, period },
      orderBy: { scoreGlobal: 'desc' },
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
    const prismaStudents = await this.prisma.student.findMany({
      where: {
        model,
        year,
        period,
      },
      orderBy: { scoreGlobal: 'desc' },
    });

    return prismaStudents.map((ps) => this.toDomain(ps));
  }

  /**
   * Buscar estudiantes destacados (puntaje >= 267 = Avanzado)
   */
  public async findHighPerformers(year: number, period: number): Promise<Student[]> {
    const prismaStudents = await this.prisma.student.findMany({
      where: {
        year,
        period,
        scoreGlobal: { gte: 267 }, // Umbral nivel Avanzado
      },
      orderBy: { scoreGlobal: 'desc' },
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
    const props: StudentProps = {
      id: prismaStudent.id,
      documentNumber: prismaStudent.documentNumber,
      fullName: prismaStudent.fullName,
      grade: prismaStudent.grade,
      model: prismaStudent.model as AcademicModel,
      year: prismaStudent.year,
      period: prismaStudent.period,
      scores: {
        reading: Score.create(prismaStudent.scoreReading),
        mathematics: Score.create(prismaStudent.scoreMathematics),
        socialSciences: Score.create(prismaStudent.scoreSocialSciences),
        naturalSciences: Score.create(prismaStudent.scoreNaturalSciences),
        english: Score.create(prismaStudent.scoreEnglish),
        global: Score.create(prismaStudent.scoreGlobal),
      },
    };

    return Student.create(props);
  }

  /**
   * Convertir de Dominio a Prisma
   */
  private toPrisma(student: Student): Omit<PrismaStudent, 'id' | 'createdAt' | 'updatedAt'> {
    const scores = student.getScores();

    return {
      documentNumber: student.getDocumentNumber(),
      fullName: student.getFullName(),
      grade: student.getGrade(),
      model: student.getModel(),
      year: student.getYear(),
      period: student.getPeriod(),
      scoreReading: scores.reading.getValue(),
      scoreMathematics: scores.mathematics.getValue(),
      scoreSocialSciences: scores.socialSciences.getValue(),
      scoreNaturalSciences: scores.naturalSciences.getValue(),
      scoreEnglish: scores.english.getValue(),
      scoreGlobal: scores.global.getValue(),
    };
  }

  /**
   * Construir cláusula WHERE desde filtros
   */
  private buildWhereClause(filters?: StudentFilters): any {
    if (!filters) return {};

    return {
      ...(filters.year && { year: filters.year }),
      ...(filters.period && { period: filters.period }),
      ...(filters.grade && { grade: filters.grade }),
      ...(filters.model && { model: filters.model }),
      ...(filters.minGlobalScore && { scoreGlobal: { gte: filters.minGlobalScore } }),
      ...(filters.maxGlobalScore && { scoreGlobal: { lte: filters.maxGlobalScore } }),
    };
  }
}

