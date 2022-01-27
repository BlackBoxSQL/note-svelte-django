<script lang="ts">
	import Note from './Note.svelte';
	import '../../app.css';
</script>

<div class="main overflow-auto pt-8 grid grid-cols-2 gap-3 py-10 pr-8 bg-secondary text-primary">
	<Note />
	<Note />
	<Note />
	<Note />
	<Note />
	<Note />
	<Note />
</div>

<style>
	.main {
		grid-area: main;
		/* background-color: #32292f; */
		height: 90vh;
	}
	/* width */
	::-webkit-scrollbar {
		width: 10px;
	}

	/* Track */
	::-webkit-scrollbar-track {
		box-shadow: inset 0 0 5px #ffa163;
		border-radius: 10px;
	}

	/* Handle */
	::-webkit-scrollbar-thumb {
		background: #ff6400;
		border-radius: 10px;
	}

	/* Handle on hover */
	::-webkit-scrollbar-thumb:hover {
		background: #ff6400;
	}
</style>
