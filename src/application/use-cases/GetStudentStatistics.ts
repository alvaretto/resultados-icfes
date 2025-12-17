/**
 * Use Case: GetStudentStatistics
 * 
 * Caso de uso para obtener estadísticas de un estudiante específico.
 * Aplicando Single Responsibility Principle y Use Case Pattern.
 * 
 * @application Análisis ICFES
 */

import { IStudentRepository } from '@/domain/repositories/IStudentRepository';
import { Student } from '@/domain/entities/Student';
import { PerformanceLevel, PerformanceLevelType } from '@/domain/value-objects/PerformanceLevel';

export interface StudentStatisticsDTO {
  student: {
    id: string;
    documentNumber: string;
    fullName: string;
    grade: number;
    model: string;
    year: number;
    period: number;
  };
  scores: {
    reading: number;
    mathematics: number;
    socialSciences: number;
    naturalSciences: number;
    english: number;
    global: number;
    average: number;
  };
  performanceLevels: {
    reading: string;
    mathematics: string;
    socialSciences: string;
    naturalSciences: string;
    english: string;
    global: string;
  };
  ranking: {
    position: number;
    total: number;
    percentile: number;
  };
  isHighPerformer: boolean;
}

/**
 * Caso de Uso: Obtener estadísticas detalladas de un estudiante
 */
export class GetStudentStatistics {
  constructor(private readonly studentRepository: IStudentRepository) {}

  /**
   * Ejecutar caso de uso
   * 
   * @param studentId - ID del estudiante
   * @returns Estadísticas del estudiante o null si no existe
   * @throws Error si hay problemas de acceso a datos
   */
  public async execute(studentId: string): Promise<StudentStatisticsDTO | null> {
    // 1. Buscar estudiante
    const student = await this.studentRepository.findById(studentId);
    
    if (!student) {
      return null;
    }

    // 2. Obtener todos los estudiantes del mismo año/período para ranking
    const allStudents = await this.studentRepository.findByYearAndPeriod(
      student.getYear(),
      student.getPeriod()
    );

    // 3. Calcular ranking
    const ranking = this.calculateRanking(student, allStudents);

    // 4. Construir DTO (Data Transfer Object)
    return this.buildDTO(student, ranking);
  }

  /**
   * Calcular posición en ranking
   */
  private calculateRanking(
    student: Student,
    allStudents: Student[]
  ): StudentStatisticsDTO['ranking'] {
    // Ordenar por puntaje global descendente
    const sorted = allStudents.sort((a, b) => {
      const scoreA = a.getScores().global.getValue();
      const scoreB = b.getScores().global.getValue();
      return scoreB - scoreA;
    });

    // Encontrar posición (1-based)
    const position = sorted.findIndex((s) => s.equals(student)) + 1;
    const total = sorted.length;
    const percentile = ((total - position + 1) / total) * 100;

    return {
      position,
      total,
      percentile: Math.round(percentile * 100) / 100,
    };
  }

  /**
   * Construir DTO desde entidad
   */
  private buildDTO(
    student: Student,
    ranking: StudentStatisticsDTO['ranking']
  ): StudentStatisticsDTO {
    const scores = student.getScores();

    return {
      student: {
        id: student.getId(),
        documentNumber: student.getDocumentNumber(),
        fullName: student.getFullName(),
        grade: student.getGrade(),
        model: student.getModel(),
        year: student.getYear(),
        period: student.getPeriod(),
      },
      scores: {
        reading: scores.reading.getValue(),
        mathematics: scores.mathematics.getValue(),
        socialSciences: scores.socialSciences.getValue(),
        naturalSciences: scores.naturalSciences.getValue(),
        english: scores.english.getValue(),
        global: scores.global.getValue(),
        average: student.getAverageScore(),
      },
      performanceLevels: {
        reading: student.getPerformanceLevelBySubject('reading').getType(),
        mathematics: student.getPerformanceLevelBySubject('mathematics').getType(),
        socialSciences: student.getPerformanceLevelBySubject('socialSciences').getType(),
        naturalSciences: student.getPerformanceLevelBySubject('naturalSciences').getType(),
        english: student.getPerformanceLevelBySubject('english').getType(),
        global: student.getGlobalPerformanceLevel().getType(),
      },
      ranking,
      isHighPerformer: student.isHighPerformer(),
    };
  }
}

