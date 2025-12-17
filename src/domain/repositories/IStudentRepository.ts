/**
 * Repository Interface: IStudentRepository
 * 
 * Define el contrato para acceso a datos de estudiantes.
 * Aplicando Dependency Inversion Principle (DIP) y Repository Pattern.
 * 
 * El dominio define la interfaz, la infraestructura la implementa.
 * 
 * @domain Análisis ICFES
 */

import { Student, AcademicModel } from '../entities/Student';

export interface StudentFilters {
  year?: number;
  period?: number;
  grade?: number;
  model?: AcademicModel;
  minGlobalScore?: number;
  maxGlobalScore?: number;
}

export interface PaginationOptions {
  page: number;
  pageSize: number;
}

export interface PaginatedResult<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
}

/**
 * Contrato del repositorio - El dominio no conoce detalles de implementación
 */
export interface IStudentRepository {
  /**
   * Buscar estudiante por ID
   */
  findById(id: string): Promise<Student | null>;

  /**
   * Buscar estudiante por documento
   */
  findByDocument(documentNumber: string): Promise<Student | null>;

  /**
   * Listar todos los estudiantes con filtros opcionales
   */
  findAll(filters?: StudentFilters): Promise<Student[]>;

  /**
   * Listar estudiantes con paginación
   */
  findAllPaginated(
    filters?: StudentFilters,
    pagination?: PaginationOptions
  ): Promise<PaginatedResult<Student>>;

  /**
   * Buscar estudiantes por año y período
   */
  findByYearAndPeriod(year: number, period: number): Promise<Student[]>;

  /**
   * Buscar estudiantes por grado
   */
  findByGrade(grade: number, year: number, period: number): Promise<Student[]>;

  /**
   * Buscar estudiantes por modelo académico
   */
  findByModel(
    model: AcademicModel,
    year: number,
    period: number
  ): Promise<Student[]>;

  /**
   * Buscar estudiantes destacados (puntaje global avanzado)
   */
  findHighPerformers(year: number, period: number): Promise<Student[]>;

  /**
   * Guardar estudiante (crear o actualizar)
   */
  save(student: Student): Promise<Student>;

  /**
   * Guardar múltiples estudiantes (bulk operation)
   */
  saveMany(students: Student[]): Promise<Student[]>;

  /**
   * Eliminar estudiante
   */
  delete(id: string): Promise<void>;

  /**
   * Contar estudiantes con filtros
   */
  count(filters?: StudentFilters): Promise<number>;

  /**
   * Verificar si existe un estudiante
   */
  exists(id: string): Promise<boolean>;
}

