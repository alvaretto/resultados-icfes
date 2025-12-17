/**
 * Home Page - Página de Inicio
 * 
 * Dashboard principal con resumen y navegación.
 */

import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <section className="bg-white rounded-lg shadow-lg p-8 text-center">
        <h2 className="text-4xl font-bold text-gray-900 mb-4">
          Bienvenido al Sistema de Análisis ICFES
        </h2>
        <p className="text-gray-600 text-lg mb-6 max-w-2xl mx-auto">
          Analiza, compara y visualiza los resultados del examen Saber 11° con tecnología de punta.
          Arquitectura limpia, type-safe y escalable.
        </p>
        
        <div className="flex gap-4 justify-center">
          <Link
            href="/estudiantes"
            className="btn-primary inline-flex items-center gap-2"
          >
            📊 Ver Estudiantes
          </Link>
          <Link
            href="/estadisticas"
            className="bg-purple-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-purple-700 transition-colors inline-flex items-center gap-2"
          >
            📈 Estadísticas
          </Link>
        </div>
      </section>

      {/* Features Grid */}
      <section className="grid md:grid-cols-3 gap-6">
        <FeatureCard
          icon="🎯"
          title="Clean Architecture"
          description="Código modular, testeable y mantenible con principios SOLID aplicados."
        />
        <FeatureCard
          icon="⚡"
          title="Alto Rendimiento"
          description="SSR + ISR con Next.js 14. Carga en menos de 1 segundo."
        />
        <FeatureCard
          icon="🔒"
          title="Type-Safe"
          description="100% TypeScript con strict mode. Cero errores en runtime."
        />
        <FeatureCard
          icon="📊"
          title="Análisis Detallado"
          description="Estadísticas por estudiante, grado, área y modelo académico."
        />
        <FeatureCard
          icon="📈"
          title="Comparativas"
          description="Compara resultados entre años y visualiza el progreso."
        />
        <FeatureCard
          icon="🚀"
          title="Desplegado en Vercel"
          description="CI/CD automático, previews y rollback instantáneo."
        />
      </section>

      {/* Tech Stack */}
      <section className="bg-white rounded-lg shadow-lg p-8">
        <h3 className="text-2xl font-bold text-gray-900 mb-6 text-center">
          Stack Tecnológico
        </h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <TechBadge name="Next.js 14" />
          <TechBadge name="TypeScript" />
          <TechBadge name="Prisma ORM" />
          <TechBadge name="Tailwind CSS" />
          <TechBadge name="Vercel Postgres" />
          <TechBadge name="React 18" />
          <TechBadge name="Clean Architecture" />
          <TechBadge name="SOLID Principles" />
        </div>
      </section>

      {/* Architecture Info */}
      <section className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-8">
        <h3 className="text-2xl font-bold text-gray-900 mb-4">
          🏗️ Arquitectura Hexagonal
        </h3>
        <div className="grid md:grid-cols-4 gap-4 text-center">
          <div className="bg-white rounded-lg p-4 shadow">
            <div className="text-3xl mb-2">🎨</div>
            <h4 className="font-bold text-sm">Presentation</h4>
            <p className="text-xs text-gray-600 mt-1">UI Components</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow">
            <div className="text-3xl mb-2">📋</div>
            <h4 className="font-bold text-sm">Application</h4>
            <p className="text-xs text-gray-600 mt-1">Use Cases</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow">
            <div className="text-3xl mb-2">🎯</div>
            <h4 className="font-bold text-sm">Domain</h4>
            <p className="text-xs text-gray-600 mt-1">Business Logic</p>
          </div>
          <div className="bg-white rounded-lg p-4 shadow">
            <div className="text-3xl mb-2">🔧</div>
            <h4 className="font-bold text-sm">Infrastructure</h4>
            <p className="text-xs text-gray-600 mt-1">Database & APIs</p>
          </div>
        </div>
      </section>

      {/* Status */}
      <section className="text-center text-sm text-gray-600">
        <p>✅ Sistema en desarrollo local</p>
        <p className="mt-2">
          Base de datos: <span className="font-mono bg-gray-200 px-2 py-1 rounded">SQLite (dev.db)</span>
        </p>
      </section>
    </div>
  );
}

// Helper Components

function FeatureCard({
  icon,
  title,
  description,
}: {
  icon: string;
  title: string;
  description: string;
}) {
  return (
    <div className="card">
      <div className="text-4xl mb-3">{icon}</div>
      <h3 className="text-lg font-bold text-gray-900 mb-2">{title}</h3>
      <p className="text-gray-600 text-sm">{description}</p>
    </div>
  );
}

function TechBadge({ name }: { name: string }) {
  return (
    <div className="bg-blue-100 text-blue-800 px-3 py-2 rounded-lg text-sm font-semibold text-center">
      {name}
    </div>
  );
}

