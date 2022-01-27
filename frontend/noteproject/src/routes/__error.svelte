<script lang="ts">
	import '../app.css';
</script>

<svelte:head>
	<title>404</title>
</svelte:head>
<div
	class="
    flex
    items-center
    justify-center
    w-screen
    h-screen
    bg-gradient-to-r
    from-orange-700
    to-orange-500
  "
>
	<div class="px-40 py-20 bg-secondary rounded-md shadow-xl">
		<div class="flex flex-col items-center">
			<h1 class="font-bold text-white text-9xl">404</h1>

			<h6 class="mb-2 text-2xl font-bold text-center text-white md:text-3xl">
				<span class="text-primary">Oops!</span> Page not found
			</h6>

			<p class="mb-8 text-center text-white md:text-lg">
				The page you’re looking for doesn’t exist.
			</p>

			<a
				href="/"
				class="px-6 py-2 text-sm font-semibold text-primary bg-secondary rounded-lg border border-primary"
				>Go home</a
			>
		</div>
	</div>
</div>
