<script lang="ts">
	import '../../app.css';
	import moment from 'moment';
	export let date_times: Date = new Date();
	export let date_time: string = moment(date_times).format('MMMM Do YYYY');
	//formate date and time like 12 september, 2021 03:45 PM
</script>

<div class="flex justify-between time font-extralight text-xs font-mono">
	<p class="flex justify-between align-baseline">
		<i><img src="/bolt.svg" alt="" width="14" height="14" class="pr-0.5 pointer" /></i>
		{date_time}
	</p>
	<button type="submit">
		<img src="/notdone.svg" alt="" width="22" height="22" class="px-0.5" />
	</button>
</div>

<style>
</style>
