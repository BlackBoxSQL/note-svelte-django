module.exports = {

	// add this section #FF6400 20C20E

	purge: ['./src/**/*.html', './src/**/*.svelte'],
	darkMode: false, // or 'media' or 'class'
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
