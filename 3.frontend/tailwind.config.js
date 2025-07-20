/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // <-- ADD THIS LINE to enable class-based dark mode
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // <-- This line is crucial
  ],
  theme: {
    extend: {
      // Here we define our custom colors
      colors: {
        'primary': '#1A1A1A',     // A dark charcoal for primary background
        'secondary': '#2A2A2A',   // A slightly lighter gray for cards/modals
        'accent': {
          DEFAULT: '#FF8C00', // Dark Orange for buttons, links, highlights
          hover: '#FFA500',   // A brighter orange for hover states
        },
        'text-primary': '#E0E0E0', // A light gray for primary text
        'text-secondary': '#B3B3B3',// A dimmer gray for secondary text
      },
    },
  },
  plugins: [],
}