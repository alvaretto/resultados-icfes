/**
 * UI Component: ScoreDisplay
 * 
 * Componente para mostrar puntajes de manera consistente.
 * Responsabilidad única: Formatear y mostrar números.
 * 
 * @presentation React Component
 */

'use client';

import { cn } from '@/presentation/utils/cn';

interface ScoreDisplayProps {
  score: number;
  size?: 'sm' | 'md' | 'lg';
  className?: string;
  showDecimals?: boolean;
}

/**
 * Display de puntaje con formato consistente
 */
export function ScoreDisplay({
  score,
  size = 'md',
  className,
  showDecimals = false,
}: ScoreDisplayProps) {
  const formattedScore = showDecimals 
    ? score.toFixed(1) 
    : Math.round(score).toString();

  const sizeClasses = {
    sm: 'text-sm',
    md: 'text-base',
    lg: 'text-lg font-bold',
  };

  return (
    <span
      className={cn(
        'tabular-nums font-semibold text-gray-900',
        sizeClasses[size],
        className
      )}
    >
      {formattedScore}
    </span>
  );
}

