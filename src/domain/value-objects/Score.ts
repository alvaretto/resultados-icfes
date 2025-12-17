/**
 * Value Object: Score (Puntaje ICFES)
 * 
 * Representa un puntaje válido del examen ICFES.
 * Aplicando Value Object Pattern y validaciones de dominio.
 * 
 * @domain Análisis ICFES
 */

export class Score {
  private static readonly MIN_SCORE = 0;
  private static readonly MAX_SCORE = 500;

  private constructor(private readonly value: number) {
    this.validate();
  }

  /**
   * Factory method con validación
   */
  public static create(value: number): Score {
    return new Score(value);
  }

  /**
   * Validación de reglas de negocio
   */
  private validate(): void {
    if (!Number.isFinite(this.value)) {
      throw new Error('El puntaje debe ser un número válido');
    }

    if (this.value < Score.MIN_SCORE) {
      throw new Error(`El puntaje no puede ser menor a ${Score.MIN_SCORE}`);
    }

    if (this.value > Score.MAX_SCORE) {
      throw new Error(`El puntaje no puede ser mayor a ${Score.MAX_SCORE}`);
    }
  }

  /**
   * Obtener el valor del puntaje
   */
  public getValue(): number {
    return this.value;
  }

  /**
   * Comparar con otro puntaje
   */
  public isGreaterThan(other: Score): boolean {
    return this.value > other.value;
  }

  /**
   * Calcular diferencia con otro puntaje
   */
  public diff(other: Score): number {
    return this.value - other.value;
  }

  /**
   * Igualdad por valor (Value Object Pattern)
   */
  public equals(other: Score): boolean {
    return this.value === other.value;
  }

  /**
   * Representación en string
   */
  public toString(): string {
    return this.value.toFixed(0);
  }
}

