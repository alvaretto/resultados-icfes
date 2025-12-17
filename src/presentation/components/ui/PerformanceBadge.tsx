/**
 * UI Component: PerformanceBadge
 * 
 * Componente de presentación para badges de nivel de desempeño.
 * Sin lógica de negocio - Solo presentación (Separation of Concerns).
 * 
 * @presentation React Component
 */

'use client';

import { PerformanceLevelType } from '@/domain/value-objects/PerformanceLevel';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/presentation/utils/cn';

/**
 * Variantes de estilos usando CVA (Class Variance Authority)
 * Aplicando Open/Closed Principle - Fácil extender sin modificar
 */
const badgeVariants = cva(
  'inline-flex items-center rounded-full font-semibold transition-colors',
  {
    variants: {
      level: {
        [PerformanceLevelType.AVANZADO]: 'bg-green-100 text-green-800',
        [PerformanceLevelType.SATISFACTORIO]: 'bg-blue-100 text-blue-800',
        [PerformanceLevelType.MINIMO]: 'bg-yellow-100 text-yellow-800',
        [PerformanceLevelType.INSUFICIENTE]: 'bg-red-100 text-red-800',
      },
      size: {
        sm: 'px-2 py-0.5 text-xs',
        md: 'px-2.5 py-1 text-sm',
        lg: 'px-3 py-1.5 text-base',
      },
    },
    defaultVariants: {
      size: 'md',
    },
  }
);

export interface PerformanceBadgeProps
  extends VariantProps<typeof badgeVariants> {
  level: string;
  className?: string;
  showIcon?: boolean;
}

/**
 * Mapeo de iconos por nivel
 */
const LEVEL_ICONS: Record<PerformanceLevelType, string> = {
  [PerformanceLevelType.AVANZADO]: '🌟',
  [PerformanceLevelType.SATISFACTORIO]: '✅',
  [PerformanceLevelType.MINIMO]: '⚠️',
  [PerformanceLevelType.INSUFICIENTE]: '❌',
};

/**
 * Mapeo de etiquetas legibles
 */
const LEVEL_LABELS: Record<PerformanceLevelType, string> = {
  [PerformanceLevelType.AVANZADO]: 'Avanzado',
  [PerformanceLevelType.SATISFACTORIO]: 'Satisfactorio',
  [PerformanceLevelType.MINIMO]: 'Mínimo',
  [PerformanceLevelType.INSUFICIENTE]: 'Insuficiente',
};

/**
 * Badge de nivel de desempeño
 * 
 * Responsabilidad única: Renderizar badge con estilos apropiados
 */
export function PerformanceBadge({
  level,
  size,
  className,
  showIcon = true,
}: PerformanceBadgeProps) {
  // Type-safe level casting
  const levelType = level as PerformanceLevelType;
  
  // Validación
  if (!Object.values(PerformanceLevelType).includes(levelType)) {
    console.warn(`Invalid performance level: ${level}`);
    return null;
  }

  const icon = LEVEL_ICONS[levelType];
  const label = LEVEL_LABELS[levelType];

  return (
    <span className={cn(badgeVariants({ level: levelType, size }), className)}>
      {showIcon && <span className="mr-1">{icon}</span>}
      {label}
    </span>
  );
}

