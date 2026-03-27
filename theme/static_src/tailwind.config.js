/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
        'dark-bg': '#0A0F16',       // Deepest background (pure app ke liye)
        'card-bg': '#161616',       // Cards aur panels ka background
        'card-hover': '#1A2333',    // Cards par hover effect ke liye
        'border-dark': '#1F2937',   // Borders aur dividers
        'accent': '#0df2f2',        // Primary Cyan/Teal color
        'accent-hover': '#04ffff',  // Button hover
        'text-muted': '#9CA3AF',    // Subtitles aur labels
        'text-darker': '#6B7280',   // Placeholder text
        'footer': '#102222',    
        'caption': '#131e1e',  //
        'input-bg': '#0f172a',  // Input fields ka background
      },
      boxShadow: {
        'neon-glow': '0 0 20px rgba(0, 229, 255, 0.2)',
        'neon-glow-strong': '0 0 30px rgba(0, 229, 255, 0.4)',
        'card': '0 10px 30px -10px rgba(0, 0, 0, 0.5)',
      },
      backgroundImage: {
        // Heading mein jo "Instantly" par color gradient hai uske liye
        'text-gradient': 'linear-gradient(to bottom, #ffffff, #000000)',
      },
      // Chhote aur smooth animations
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        pulseGlow: {
          '0%, 100%': { boxShadow: '0 0 15px rgba(0, 229, 255, 0.2)' },
          '50%': { boxShadow: '0 0 25px rgba(0, 229, 255, 0.5)' },
        }
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'slide-up': 'slideUp 0.6s ease-out forwards',
        'slide-up-delay': 'slideUp 0.6s ease-out 0.2s forwards', // Thoda delay se aane ke liye
        'pulse-glow': 'pulseGlow 2s infinite',
      },
      borderRadius: {
        'btn': '30px', // Ab aapki custom class ban gayi
      }
        },
    },
    plugins: [],
}
