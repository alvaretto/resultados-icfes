/**
 * Utility: cn (classnames utility)
 * 
 * Función para combinar classNames de manera eficiente.
 * Usa clsx para condicionales y tailwind-merge para evitar conflictos.
 * 
 * @presentation Utility Function
 */

import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Combinar clases de TailwindCSS evitando conflictos
 * 
 * @param inputs - Array de clases o condicionales
 * @returns String de clases optimizado
 * 
 * @example
 * cn('px-2 py-1', condition && 'bg-blue-500', 'text-white')
 * cn({ 'bg-red-500': error, 'bg-green-500': success })
 */
export function cn(...inputs: ClassValue[]): string {
  return twMerge(clsx(inputs));
}

