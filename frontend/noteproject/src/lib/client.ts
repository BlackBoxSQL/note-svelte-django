import { InMemoryCache } from '@apollo/client/core';
import { SvelteApolloClient } from 'svelte-apollo-client';

const tokenn = localStorage.getItem('token');
// if (tokenn == null) {
// 	location.href = '/login';
// } else {
// 	location.href = '/';
// }
export const client = SvelteApolloClient({
	uri: 'http://127.0.0.1:8000/graphql',
	cache: new InMemoryCache(),
	headers: {
		Authorization: tokenn ? `JWT ${tokenn}` : ''
	}
});
