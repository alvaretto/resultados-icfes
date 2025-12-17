/**
 * Value Object: PerformanceLevel (Nivel de Desempeño)
 * 
 * Representa los niveles de desempeño según criterios del ICFES.
 * Encapsula la lógica de clasificación de desempeño.
 * 
 * @domain Análisis ICFES
 */

export enum PerformanceLevelType {
  INSUFICIENTE = 'INSUFICIENTE',
  MINIMO = 'MINIMO',
  SATISFACTORIO = 'SATISFACTORIO',
  AVANZADO = 'AVANZADO',
}

interface PerformanceLevelThresholds {
  min: number;
  max: number;
  level: PerformanceLevelType;
  description: string;
  color: string;
}

export class PerformanceLevel {
  // Umbrales oficiales del ICFES (Single Source of Truth)
  private static readonly THRESHOLDS: PerformanceLevelThresholds[] = [
    {
      min: 267,
      max: 500,
      level: PerformanceLevelType.AVANZADO,
      description: 'El estudiante supera las expectativas de aprendizaje',
      color: '#22c55e', // success-500
    },
    {
      min: 233,
      max: 266,
      level: PerformanceLevelType.SATISFACTORIO,
      description: 'El estudiante alcanza las expectativas de aprendizaje',
      color: '#0ea5e9', // primary-500
    },
    {
      min: 200,
      max: 232,
      level: PerformanceLevelType.MINIMO,
      description: 'El estudiante está próximo a alcanzar las expectativas',
      color: '#eab308', // warning-500
    },
    {
      min: 0,
      max: 199,
      level: PerformanceLevelType.INSUFICIENTE,
      description: 'El estudiante no supera las preguntas de menor complejidad',
      color: '#ef4444', // danger-500
    },
  ];

  private constructor(
    private readonly type: PerformanceLevelType,
    private readonly description: string,
    private readonly color: string
  ) {}

  /**
   * Factory method - Clasificar puntaje en nivel de desempeño
   * 
   * @param score - Puntaje a clasificar
   * @returns PerformanceLevel correspondiente
   */
  public static fromScore(score: number): PerformanceLevel {
    const threshold = this.THRESHOLDS.find(
      (t) => score >= t.min && score <= t.max
    );

    if (!threshold) {
      throw new Error(`Puntaje fuera de rango: ${score}`);
    }

    return new PerformanceLevel(
      threshold.level,
      threshold.description,
      threshold.color
    );
  }

  /**
   * Obtener tipo de nivel
   */
  public getType(): PerformanceLevelType {
    return this.type;
  }

  /**
   * Obtener descripción
   */
  public getDescription(): string {
    return this.description;
  }

  /**
   * Obtener color asociado
   */
  public getColor(): string {
    return this.color;
  }

  /**
   * Verificar si es nivel avanzado
   */
  public isAdvanced(): boolean {
    return this.type === PerformanceLevelType.AVANZADO;
  }

  /**
   * Verificar si es nivel insuficiente
   */
  public isInsufficient(): boolean {
    return this.type === PerformanceLevelType.INSUFICIENTE;
  }

  /**
   * Comparar niveles
   */
  public isBetterThan(other: PerformanceLevel): boolean {
    const order = [
      PerformanceLevelType.INSUFICIENTE,
      PerformanceLevelType.MINIMO,
      PerformanceLevelType.SATISFACTORIO,
      PerformanceLevelType.AVANZADO,
    ];

    return order.indexOf(this.type) > order.indexOf(other.type);
  }

  /**
   * Igualdad
   */
  public equals(other: PerformanceLevel): boolean {
    return this.type === other.type;
  }

  /**
   * Representación en string
   */
  public toString(): string {
    return this.type;
  }
}

