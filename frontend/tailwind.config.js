/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        botola: {
          green: '#1B5E20',
          orange: '#FF6F00',
          purple: '#6A1B9A', // Inwi purple
        }
      },
      fontFamily: {
        sans: ['Roboto', 'sans-serif'],
        display: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}