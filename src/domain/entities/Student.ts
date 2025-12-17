/**
 * Entity: Student (Estudiante)
 * 
 * Entidad del dominio que representa un estudiante con sus resultados ICFES.
 * Aplica Domain-Driven Design principles.
 * 
 * @domain Análisis ICFES
 */

import { Score } from '../value-objects/Score';
import { PerformanceLevel } from '../value-objects/PerformanceLevel';

export enum AcademicModel {
  REGULAR = 'REGULAR',
  FLEXIBLE = 'FLEXIBLE',
}

export interface StudentScores {
  reading: Score;
  mathematics: Score;
  socialSciences: Score;
  naturalSciences: Score;
  english: Score;
  global: Score;
}

export interface StudentProps {
  id: string;
  documentNumber: string;
  fullName: string;
  grade: number;
  model: AcademicModel;
  year: number;
  period: number;
  scores: StudentScores;
}

export class Student {
  private constructor(private readonly props: StudentProps) {
    this.validate();
  }

  /**
   * Factory method con validación
   */
  public static create(props: StudentProps): Student {
    return new Student(props);
  }

  /**
   * Validaciones de negocio
   */
  private validate(): void {
    if (!this.props.id || this.props.id.trim() === '') {
      throw new Error('El ID del estudiante es requerido');
    }

    if (!this.props.documentNumber || this.props.documentNumber.trim() === '') {
      throw new Error('El número de documento es requerido');
    }

    if (!this.props.fullName || this.props.fullName.trim() === '') {
      throw new Error('El nombre completo es requerido');
    }

    if (this.props.grade < 10 || this.props.grade > 11) {
      throw new Error('El grado debe ser 10 u 11');
    }

    if (this.props.year < 2020 || this.props.year > 2030) {
      throw new Error('Año fuera de rango válido');
    }
  }

  // Getters (Encapsulación)
  
  public getId(): string {
    return this.props.id;
  }

  public getDocumentNumber(): string {
    return this.props.documentNumber;
  }

  public getFullName(): string {
    return this.props.fullName;
  }

  public getGrade(): number {
    return this.props.grade;
  }

  public getModel(): AcademicModel {
    return this.props.model;
  }

  public getYear(): number {
    return this.props.year;
  }

  public getPeriod(): number {
    return this.props.period;
  }

  public getScores(): StudentScores {
    return { ...this.props.scores }; // Defensive copy
  }

  /**
   * Lógica de dominio: Calcular nivel de desempeño por área
   */
  public getPerformanceLevelBySubject(
    subject: keyof Omit<StudentScores, 'global'>
  ): PerformanceLevel {
    const score = this.props.scores[subject].getValue();
    return PerformanceLevel.fromScore(score);
  }

  /**
   * Lógica de dominio: Calcular nivel de desempeño global
   */
  public getGlobalPerformanceLevel(): PerformanceLevel {
    const globalScore = this.props.scores.global.getValue();
    return PerformanceLevel.fromScore(globalScore);
  }

  /**
   * Lógica de dominio: Verificar si es estudiante destacado
   */
  public isHighPerformer(): boolean {
    return this.getGlobalPerformanceLevel().isAdvanced();
  }

  /**
   * Lógica de dominio: Comparar con otro estudiante
   */
  public hasBetterScoreThan(other: Student): boolean {
    return this.props.scores.global.isGreaterThan(other.props.scores.global);
  }

  /**
   * Lógica de dominio: Calcular promedio de áreas
   */
  public getAverageScore(): number {
    const { reading, mathematics, socialSciences, naturalSciences, english } = this.props.scores;
    
    const scores = [
      reading.getValue(),
      mathematics.getValue(),
      socialSciences.getValue(),
      naturalSciences.getValue(),
      english.getValue(),
    ];

    return scores.reduce((sum, score) => sum + score, 0) / scores.length;
  }

  /**
   * Igualdad por ID (Entity Pattern)
   */
  public equals(other: Student): boolean {
    return this.props.id === other.props.id;
  }

  /**
   * Serialización para persistencia
   */
  public toJSON(): Record<string, any> {
    return {
      id: this.props.id,
      documentNumber: this.props.documentNumber,
      fullName: this.props.fullName,
      grade: this.props.grade,
      model: this.props.model,
      year: this.props.year,
      period: this.props.period,
      scores: {
        reading: this.props.scores.reading.getValue(),
        mathematics: this.props.scores.mathematics.getValue(),
        socialSciences: this.props.scores.socialSciences.getValue(),
        naturalSciences: this.props.scores.naturalSciences.getValue(),
        english: this.props.scores.english.getValue(),
        global: this.props.scores.global.getValue(),
      },
    };
  }
}

