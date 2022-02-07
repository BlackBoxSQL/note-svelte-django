<script lang="ts">
	import '../../app.css';
	export let time: Date = new Date();
</script>

<div class="flex justify-between time font-extralight text-xs font-mono">
	<p class="flex justify-between align-baseline">
		<i><img src="/bolt.svg" alt="" width="14" height="14" class="pr-0.5 pointer" /></i>
		{time.getFullYear()}-{time.getMonth() + 1}-{time.getDate()}
	</p>
	<button type="submit">
		<img src="/notdone.svg" alt="" width="22" height="22" class="px-0.5" />
	</button>
</div>

<style>
</style>
