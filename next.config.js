/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  // Temporarily disabled for initial deploy
  // experimental: {
  //   typedRoutes: true,
  // },
  env: {
    APP_NAME: 'Análisis ICFES - Pedacito de Cielo',
    APP_VERSION: '2.0.0',
  },
  images: {
    domains: [],
    formats: ['image/avif', 'image/webp'],
  },
};

module.exports = nextConfig;

