/** @type {import('next').NextConfig} */
const nextConfig = {
  // images: {
  //   domains: [
  //     "images.unsplash.com",
  //     "cdn.pixabay.com",
  //     "images.pexel.com",
  //     "source.unsplash.com",
  //   ],
  // },
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '*',
      },
      {
        protocol: 'http',
        hostname: 'localhost',
      },
    ],
  },
};

module.exports = nextConfig;
