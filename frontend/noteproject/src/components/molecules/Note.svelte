<script lang="ts">
	import Memo from '../atoms/Memo.svelte';
	import TimeShow from '../atoms/TimeShow.svelte';
	import Title from '../atoms/Title.svelte';
	import '../../app.css';
	import ApolloClient from 'apollo-boost';
	import { setClient, getClient, query } from 'svelte-apollo';
	import { gql } from 'apollo-boost';
</script>

<div class="h-fit w-fit px-1 py-1  shadow-md hover:border hover:rounded-md hover:border-primary">
	<TimeShow />
	<Title />
	<Memo
		memo={'I Lorem ipsum, dolor sit amet consectetur adipisicing elit. Amet mollitia, eius sunt aut cupiditate saepe ut voluptates ad neque aperiam consectetur officia quia fugiat sequi quis, soluta, dolorem repellendus qui?'}
	/>
</div>

<style>
</style>
