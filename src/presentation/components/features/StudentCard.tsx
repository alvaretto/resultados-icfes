/**
 * Feature Component: StudentCard
 * 
 * Componente para mostrar información de un estudiante.
 * Aplicando Component Composition y Single Responsibility.
 * 
 * @presentation React Component
 */

'use client';

import { StudentStatisticsDTO } from '@/application/use-cases/GetStudentStatistics';
import { PerformanceBadge } from '../ui/PerformanceBadge';
import { ScoreDisplay } from '../ui/ScoreDisplay';

interface StudentCardProps {
  statistics: StudentStatisticsDTO;
  className?: string;
}

/**
 * Componente de tarjeta de estudiante
 * 
 * Responsabilidad única: Renderizar información del estudiante
 */
export function StudentCard({ statistics, className = '' }: StudentCardProps) {
  const { student, scores, performanceLevels, ranking, isHighPerformer } = statistics;

  return (
    <div className={`bg-white rounded-lg shadow-md p-6 ${className}`}>
      {/* Header */}
      <StudentCardHeader
        fullName={student.fullName}
        documentNumber={student.documentNumber}
        grade={student.grade}
        model={student.model}
        isHighPerformer={isHighPerformer}
      />

      {/* Scores */}
      <StudentCardScores
        scores={scores}
        performanceLevels={performanceLevels}
      />

      {/* Ranking */}
      <StudentCardRanking ranking={ranking} />
    </div>
  );
}

/**
 * Sub-componente: Header (Composición)
 */
function StudentCardHeader({
  fullName,
  documentNumber,
  grade,
  model,
  isHighPerformer,
}: {
  fullName: string;
  documentNumber: string;
  grade: number;
  model: string;
  isHighPerformer: boolean;
}) {
  return (
    <div className="border-b pb-4 mb-4">
      <div className="flex justify-between items-start">
        <div>
          <h3 className="text-xl font-bold text-gray-900">{fullName}</h3>
          <p className="text-sm text-gray-600">Documento: {documentNumber}</p>
          <p className="text-sm text-gray-600">
            Grado {grade}° - {model}
          </p>
        </div>
        {isHighPerformer && (
          <span className="bg-yellow-100 text-yellow-800 px-3 py-1 rounded-full text-xs font-semibold">
            ⭐ Destacado
          </span>
        )}
      </div>
    </div>
  );
}

/**
 * Sub-componente: Scores (Composición)
 */
function StudentCardScores({
  scores,
  performanceLevels,
}: {
  scores: StudentStatisticsDTO['scores'];
  performanceLevels: StudentStatisticsDTO['performanceLevels'];
}) {
  const subjects = [
    { key: 'reading', label: 'Lectura Crítica' },
    { key: 'mathematics', label: 'Matemáticas' },
    { key: 'socialSciences', label: 'Sociales' },
    { key: 'naturalSciences', label: 'Ciencias' },
    { key: 'english', label: 'Inglés' },
  ] as const;

  return (
    <div className="space-y-3 mb-4">
      {subjects.map(({ key, label }) => (
        <div key={key} className="flex justify-between items-center">
          <span className="text-sm font-medium text-gray-700">{label}</span>
          <div className="flex items-center gap-2">
            <ScoreDisplay score={scores[key]} />
            <PerformanceBadge level={performanceLevels[key]} />
          </div>
        </div>
      ))}

      {/* Global Score - Destacado */}
      <div className="border-t pt-3 mt-3">
        <div className="flex justify-between items-center">
          <span className="text-base font-bold text-gray-900">Puntaje Global</span>
          <div className="flex items-center gap-2">
            <ScoreDisplay score={scores.global} size="lg" />
            <PerformanceBadge level={performanceLevels.global} size="lg" />
          </div>
        </div>
      </div>
    </div>
  );
}

/**
 * Sub-componente: Ranking (Composición)
 */
function StudentCardRanking({
  ranking,
}: {
  ranking: StudentStatisticsDTO['ranking'];
}) {
  return (
    <div className="bg-gray-50 rounded-lg p-3">
      <p className="text-sm text-gray-700">
        <span className="font-semibold">Posición:</span> {ranking.position} de {ranking.total}
      </p>
      <p className="text-sm text-gray-700">
        <span className="font-semibold">Percentil:</span> {ranking.percentile}%
      </p>
    </div>
  );
}

