<script lang="ts">
	import '../app.css';
	import { client } from '$lib/client';
	import { gql } from '@apollo/client/core';
	import { goto } from '$app/navigation';
	//import Cookies from 'js-cookie';
	let data = client.query(gql`
		query {
			meNotes {
				created
				title
				memo
				complete
				important
			}
		}
	`);
	console.log('index page');
</script>

<svelte:head>
	<title>Notium</title>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
	<link
		href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
		rel="stylesheet"
	/>
</svelte:head>
<div
	class="container selection:bg-primary selection:text-secondary antialiased text-primary bg-secondary"
>
	<div class="nav text-primary bg-secondary">
		<div class="logo text-primary bg-secondary flex justify-end gap-1">
			<img src="/logo3.svg" alt="" height="26" width="26" />
			<p class="font-black text-xl">Notium</p>
		</div>
		<div class="links-menu text-primary bg-secondary font-medium text-xl ">
			<a href="/">all</a>
			<a href="/complete">complete</a>
			<a href="/important">important</a>
		</div>
		<div class="exit text-primary bg-secondary">
			<a href="/login"><img src="/logout.svg" alt="" height="22" width="22" /></a>
		</div>
	</div>
	<div class="side text-primary bg-secondary">
		<div class="form bg-secondary">
			<div class="bg-secondary">
				<form class="text-primary bg-secondary grid grid-cols-1 gap-3 content-evenly mx-12 mt-7">
					<label class="bg-secondary text-base font-semibold" for="title_id">Title</label>
					<input
						maxlength="30"
						id="title_id"
						type="text"
						class="border-primary text-primary focus:border-primary focus:text-primary m-0 block w-full rounded border border-solid bg-inherit bg-clip-padding px-3 py-1.5 text-sm font-extralight transition ease-in-out placeholder-shown:bg-inherit focus:bg-inherit focus:font-bold focus:outline-none"
						placeholder="Title here..."
					/>
					<label class="bg-secondary text-base font-semibold" for="memo_id">Memo</label>
					<textarea
						maxlength="500"
						id="memo_id"
						class="border-primary text-primary focus:border-primary focus:text-primary m-0 block w-full rounded border border-solid bg-inherit bg-clip-padding px-3 py-1.5 text-sm font-extralight transition ease-in-out placeholder-shown:bg-inherit focus:bg-inherit focus:font-bold focus:outline-none"
						rows="5"
						cols="50"
						placeholder="Details here...."
					/>
					<br />
					<div class="max-w-sm">
						<label class="inline-flex items-center text-primary text-base font-semibold">
							<input
								class="text-primary w-5 h-5 mr-2 focus:primary focus:ring-primary border border-primary rounded"
								type="checkbox"
							/>
							Important
						</label>
					</div>
					<button
						class="bg-primary text-secondary rounded-xl font-base text-xl h-8 min-w-full text-center"
						>Save</button
					>
				</form>
			</div>
		</div>
		<div class="footer-frm grid grid-cols-1 text-primary bg-secondary">
			<p class="text-xs font-thin">
				Copyright © 2022 all rights reserved by <span class="font-semibold">Notium</span>
			</p>
		</div>
	</div>
	<!-- note space -->
	<div class="main overflow-auto pt-8 grid grid-cols-3 gap-3 py-10 pr-8 bg-secondary text-primary">
		<!-- for each -->
		{#if $data.loading}
			<div>loading</div>
		{:else if $data.error}
			Error {$data.error}
		{:else}
			{#each $data.data.meNotes as note}
				<div
					class="h-fit max-w-fit px-1 py-1  shadow-md hover:border hover:rounded-md hover:border-primary break-words"
				>
					<div class="flex justify-between font-extralight text-xs font-mono whitespace-pre-line">
						<p class="flex justify-between align-baseline">
							<i><img src="/idea.svg" alt="" width="22" height="22" class="pr-0.5" /></i>
						</p>
						<button type="submit">
							<img src="/task--complete.svg" alt="" width="22" height="22" class="px-0.5" />
						</button>
					</div>
					<div>
						<p class="text-xs font-extralight">{note.created}</p>
					</div>
					<div>
						<h1 class="text-base font-extrabold">{note.title}</h1>
					</div>
					<div>
						<p class="text-sm pt-1 font-light">
							{note.memo}
						</p>
					</div>
					<div class="flex justify-end gap-2">
						<button type="submit">
							<img src="/request-quote.svg" alt="" width="22" height="22" class="px-0.5" />
						</button>
						<button type="submit">
							<img src="/trash-can.svg" alt="" width="22" height="22" class="px-0.5" />
						</button>
					</div>
				</div>
			{/each}
		{/if}

		<!--for each -->
	</div>
	<!-- note space -->
</div>

<style>
	.main {
		grid-area: main;
		height: 90vh;
	}
	/* width */
	::-webkit-scrollbar {
		width: 10px;
	}

	/* Track */
	::-webkit-scrollbar-track {
		box-shadow: inset 0 0 5px #6faddc;
		border-radius: 10px;
	}

	/* Handle */
	::-webkit-scrollbar-thumb {
		background: #467599;
		border-radius: 10px;
	}

	/* Handle on hover */
	::-webkit-scrollbar-thumb:hover {
		background: #467599;
	}
	.container {
		position: fixed;
		max-width: 100vw;
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
		height: 60px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0 auto;
		width: 95%;
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
	}

	.form {
		grid-area: form;
	}

	.footer-frm {
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
