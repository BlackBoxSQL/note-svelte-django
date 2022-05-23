<script context="module">
</script>

<script>
	import NoteContain from '../components/molecules/NoteContain.svelte';
	import '../app.css';
	import { client } from '$lib/client';
	import { gql } from '@apollo/client/core';
	import { onMount } from 'svelte';
	export let notes = undefined;
	function getNotes() {
		notes = client.query(gql`
			query GetNotes {
				allCompleteNotes {
					title
					memo
				}
			}
		`);
	}
	onMount(() => {
		getNotes();
	});
</script>

<svelte:head>
	<title>Notium</title>
</svelte:head>

<div
	class="container selection:bg-primary selection:text-secondary antialiased text-primary bg-secondary"
>
	<div class="nav font-bold text-primary bg-secondary">
		<div class="logo text-primary bg-secondary">
			<img src="/logo2.svg" alt="" />
		</div>
		<div class="links-menu text-primary bg-secondary">
			<a href="/">all</a>
			<a href="/complete">complete</a>
			<a href="/important">important</a>
		</div>
		<div class="exit text-primary bg-secondary">
			<a href="/auth/login"><img src="/exit.svg" alt="" /></a>
		</div>
	</div>
	<div class="side text-primary bg-secondary">
		<div class="form bg-secondary">
			<div class="bg-secondary">
				<div class="form-control text-primary bg-secondary mx-12 mt-7 font-normal">
					<!-- svelte-ignore a11y-label-has-associated-control -->
					<label class="label">
						<span class="label-text text-primary bg-secondary">Title</span>
					</label>
					<input
						type="text"
						placeholder="Title.."
						class="input todo input-ghost text-primary bg-secondary font-thin"
					/>
					<!-- svelte-ignore a11y-label-has-associated-control -->
					<label class="label text-primary bg-secondary ">
						<span class="label-text text-primary bg-secondary ">Memo</span>
					</label>
					<textarea
						class="text-primary bg-secondary textarea h-30 h-24 textareaa textarea-ghost font-thin"
						placeholder="Write here ..."
					/>

					<button
						class="bg-primary text-secondary h-8 rounded-md font-bold mt-4 shadow-sm shadow-primary"
						>ADD</button
					>
				</div>
			</div>
		</div>
		<div
			class="footer-frm py-10 grid grid-cols-2 justify-center items-center text-primary bg-secondary"
		>
			<div class="cursor-pointer ">
				<p>Complete <span>23</span></p>
			</div>
			<div class="cursor-pointer ">
				<p>All <span>23</span></p>
			</div>
		</div>
	</div>
	<div>
		{#if notes}
			{#if $notes.loading}
				Loading...
			{:else if $notes.error}
				Error: {$notes.error.message}
			{:else}
				{#each $notes.data.allCompleteNotes || [] as note}
					<h2>Title {note.title}</h2>
					<p>Memo {note.memo}</p>
				{/each}
			{/if}
		{/if}
	</div>
</div>

<style>
	.container {
		position: fixed;
		/* background-color: #32292f; */
		max-width: 100vw;
		/* color: #ff6400; */
		display: grid;
		grid-template-columns: 0.8fr 1.2fr 1fr;
		grid-template-rows: 0.3fr 1.7fr 1fr;
		gap: 0px 0px;
		grid-auto-flow: row;
		grid-template-areas:
			'nav nav nav'
			'side main main'
			'side main main';
	}

	.nav {
		grid-area: nav;
		/* background-color: #32292f; */
		height: 60px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0 auto;
		width: 94%;
	}

	.side {
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: 1.7fr 0.3fr;
		gap: 0px 0px;
		grid-auto-flow: row;
		grid-template-areas:
			'form'
			'footer-frm';
		grid-area: side;
		height: 91vh;
		/* background-color: #32292f; */
	}

	.form {
		grid-area: form;
		/* background-color: #32292f; */
	}

	.footer-frm {
		/* background-color: #32292f; */
		justify-items: center;
		align-items: center;
	}

	.links-menu {
		align-items: center;
		padding: 0px 5px;
		word-wrap: normal;
		text-decoration: none;
		width: 250px;
		justify-content: space-evenly;
		align-content: space-around;
		display: flex;
	}

	.exit {
		cursor: pointer;
	}

	.logo {
		cursor: pointer;
	}
	/* .active {
		text-decoration: underline;
	} */
</style>
