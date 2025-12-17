/**
 * Root Layout - Next.js App Router
 * 
 * Layout principal de la aplicación con configuración global.
 */

import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });

export const metadata: Metadata = {
  title: 'Análisis ICFES - Pedacito de Cielo',
  description: 'Sistema de análisis de resultados ICFES Saber 11°',
  keywords: ['ICFES', 'Saber 11', 'Análisis', 'Educación'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es" className={inter.variable}>
      <body className="bg-gray-50 min-h-screen">
        <header className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-6 shadow-lg">
          <div className="container mx-auto px-4">
            <h1 className="text-3xl font-bold">📊 Análisis ICFES</h1>
            <p className="text-blue-100 text-sm mt-1">
              Institución Educativa Pedacito de Cielo
            </p>
          </div>
        </header>
        
        <main className="container mx-auto px-4 py-8">
          {children}
        </main>
        
        <footer className="bg-gray-800 text-gray-300 py-6 mt-12">
          <div className="container mx-auto px-4 text-center">
            <p className="text-sm">
              © 2025 IE Pedacito de Cielo - La Tebaida, Quindío
            </p>
            <p className="text-xs mt-2 text-gray-400">
              Clean Architecture con Next.js 14 + TypeScript
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}

