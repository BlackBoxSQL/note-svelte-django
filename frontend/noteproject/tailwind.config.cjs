module.exports = {
	// add this section #FF6400 20C20E primary: '#FF6400',
	// secondary: '#32292F'
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			fontFamily: {
				univers: ["'Segoe UI Regular'"],
			},
			colors: {
				primary: '#467599',
				secondary: '#E9FFF9'
			}
		}
	},
	variants: {
		extend: {}
	},
	plugins: [
		require('@tailwindcss/forms'),
	]
};