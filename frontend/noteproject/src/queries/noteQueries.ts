import { gql } from 'apollo-boost';

const GET_ALL_NOTES = gql`
	query {
		allNote {
			id
			title
			memo
			created
			complete
			important
		}
	}
`;

export { GET_ALL_NOTES };
