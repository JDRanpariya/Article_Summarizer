import { ApolloClient, HttpLink, InMemoryCache } from '@apollo/client';
import getConfig from 'next/config';

const { publicRuntimeConfig } = getConfig();

function createApolloClient() {
  return new ApolloClient({
    ssrMode: typeof window === 'undefined',
    link: new HttpLink({
        // Use Backend URL 'https://article-summarizerv1.herokuapp.com/graphql/', // e.g. https://www.myapi.com/api/v2
        uri: 'http://localhost:8000/graphql/' 
    }),
    cache: new InMemoryCache(),
  });
}

export default createApolloClient;
