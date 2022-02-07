<script lang="ts">
	import ButtonSet from './ButtonSet.svelte';
	export let memo: string = ' ';
</script>

<div class="memo text-sm pt-1 font-thin">
	<p>
		{memo}
	</p>
</div>
<ButtonSet />

<style>
</style>
