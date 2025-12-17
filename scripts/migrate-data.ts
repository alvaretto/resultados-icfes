/**
 * Script de migración de datos desde Excel a PostgreSQL
 * 
 * Este script:
 * 1. Lee los archivos Excel de resultados ICFES
 * 2. Carga los datos en la base de datos PostgreSQL de Vercel
 * 3. Mantiene la estructura de Clean Architecture
 */

import * as XLSX from 'xlsx';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

interface ExcelRow {
  'Grupo': string;
  'Primer Apellido': string;
  'Segundo Apellido': string;
  'Primer Nombre': string;
  'Segundo Nombre'?: string;
  'Tipo documento': string;
  'Número de documento': number | string;
  'Lectura Crítica': number;
  'Matemáticas': number;
  'Sociales y Ciudadanas': number;
  'Ciencias Naturales': number;
  'Inglés': number;
  'Puntaje Global': number;
}

interface DataFile {
  path: string;
  modelo: 'Regular' | 'Flexible';
  anio: number;
}

const DATA_FILES: DataFile[] = [
  {
    path: 'data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx',
    modelo: 'Regular',
    anio: 2025,
  },
  {
    path: 'data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx',
    modelo: 'Flexible',
    anio: 2025,
  },
];

async function limpiarBaseDeDatos() {
  console.log('\n🗑️  Limpiando base de datos...');

  try {
    await prisma.student.deleteMany({});
    console.log('✅ Base de datos limpiada');
  } catch (error) {
    console.error('❌ Error al limpiar base de datos:', error);
    throw error;
  }
}

async function migrarArchivo(dataFile: DataFile) {
  console.log(`\n${'='.repeat(80)}`);
  console.log(`📊 Migrando: ${dataFile.path}`);
  console.log(`   Modelo: ${dataFile.modelo} | Año: ${dataFile.anio}`);
  console.log('='.repeat(80));

  try {
    // Leer archivo Excel
    const workbook = XLSX.readFile(dataFile.path);
    const firstSheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[firstSheetName];
    
    // Convertir a JSON
    const data: ExcelRow[] = XLSX.utils.sheet_to_json(worksheet);
    
    console.log(`📋 Total de registros encontrados: ${data.length}`);
    
    let insertados = 0;
    let errores = 0;
    
    // Insertar cada estudiante
    for (const row of data) {
      try {
        // Validar que tenga datos mínimos
        if (!row['Primer Apellido'] || !row['Primer Nombre'] || !row['Número de documento']) {
          console.log(`⚠️  Saltando fila sin datos completos`);
          continue;
        }
        
        await prisma.student.create({
          data: {
            primerApellido: row['Primer Apellido'],
            segundoApellido: row['Segundo Apellido'] || '',
            primerNombre: row['Primer Nombre'],
            segundoNombre: row['Segundo Nombre'] || '',
            tipoDocumento: row['Tipo documento'],
            numeroDocumento: String(row['Número de documento']),
            grupo: row['Grupo'],
            modelo: dataFile.modelo,
            anio: dataFile.anio,
            lecturaCritica: row['Lectura Crítica'] || 0,
            matematicas: row['Matemáticas'] || 0,
            socialesCiudadanas: row['Sociales y Ciudadanas'] || 0,
            cienciasNaturales: row['Ciencias Naturales'] || 0,
            ingles: row['Inglés'] || 0,
            puntajeGlobal: row['Puntaje Global'] || 0,
          },
        });
        
        insertados++;
        
        if (insertados % 10 === 0) {
          console.log(`   ✅ ${insertados} estudiantes insertados...`);
        }
      } catch (error: any) {
        errores++;
        console.error(`   ❌ Error al insertar estudiante:`, error.message);
      }
    }
    
    console.log(`\n✅ Migración completada:`);
    console.log(`   - Insertados: ${insertados}`);
    console.log(`   - Errores: ${errores}`);
    
  } catch (error) {
    console.error(`❌ Error al migrar archivo ${dataFile.path}:`, error);
    throw error;
  }
}

async function main() {
  console.log('\n🚀 INICIANDO MIGRACIÓN DE DATOS ICFES');
  console.log('='.repeat(80));
  
  try {
    // Limpiar base de datos
    await limpiarBaseDeDatos();
    
    // Migrar cada archivo
    for (const dataFile of DATA_FILES) {
      await migrarArchivo(dataFile);
    }
    
    // Mostrar resumen final
    const totalEstudiantes = await prisma.student.count();
    console.log(`\n${'='.repeat(80)}`);
    console.log(`🎉 MIGRACIÓN COMPLETADA EXITOSAMENTE`);
    console.log(`📊 Total de estudiantes en la base de datos: ${totalEstudiantes}`);
    console.log('='.repeat(80));
    
  } catch (error) {
    console.error('\n❌ Error durante la migración:', error);
    process.exit(1);
  } finally {
    await prisma.$disconnect();
  }
}

main();

