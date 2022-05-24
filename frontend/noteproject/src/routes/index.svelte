<script context="module">
</script>

<script>
	// @ts-nocheck
	import '../app.css';
	import { client } from '$lib/client';
	import { gql } from '@apollo/client/core';
	import { Jumper } from 'svelte-loading-spinners';
	let data = client.query(gql`
		query {
			allCompleteNotes {
				title
				memo
			}
		}
	`);
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
	<!-- note space -->
	<div class="main overflow-auto pt-8 grid grid-cols-3 gap-3 py-10 pr-8 bg-secondary text-primary">
		<!-- for each -->
		<div
			class="h-fit w-fit px-1 py-1  shadow-md hover:border hover:rounded-md hover:border-primary"
		>
			<div class="flex justify-between time font-extralight text-xs font-mono">
				<p class="flex justify-between align-baseline">
					<i><img src="/bolt.svg" alt="" width="14" height="14" class="pr-0.5 pointer" /></i>
				</p>
				<button type="submit">
					<img src="/notdone.svg" alt="" width="22" height="22" class="px-0.5" />
				</button>
			</div>
			<div>
				<h3 class="font-bold font-sans">Need to pick up Zara from School</h3>
			</div>
			<div>
				<p class="text-sm pt-1 font-thin font-sans">
					I Lorem ipsum, dolor sit amet consectetur adipisicing elit. Amet mollitia, eius sunt aut
					cupiditate saepe ut voluptates ad neque aperiam consectetur officia quia fugiat sequi
					quis, soluta, dolorem repellendus qui?
				</p>
			</div>
			<div class="flex justify-end gap-2">
				<button type="submit">
					<img src="/edit.svg" alt="" width="20" height="20" class="px-0.5" />
				</button>
				<button type="submit">
					<img src="/trash-alt.svg" alt="" width="18" height="18" class="px-0.5" />
				</button>
			</div>
		</div>
		<!--for each -->
	</div>
	<!-- note space -->
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
		/*background: #ff6400;*/
		background: #ff6400;
		border-radius: 10px;
	}

	/* Handle on hover */
	::-webkit-scrollbar-thumb:hover {
		background: #ff6400;
	}
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
