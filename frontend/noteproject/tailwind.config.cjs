module.exports = {
	// add this section #FF6400 20C20E primary: '#FF6400',
	// secondary: '#32292F'
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				primary: '#FF6400',
				secondary: '#32292F'
			}
		}
	},
	variants: {
		extend: {}
	},
	plugins: [require('daisyui')]
};
