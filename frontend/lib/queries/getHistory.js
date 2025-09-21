  
import gql from 'graphql-tag';

const GET_HISTORY_SUMMARY = gql`
{
    allarticles{
      id
      summary
      content
      createdAt
    }
  }
`;

const GET_RECENT_SUMMARYS = gql`
{
    recentArticles{
      id
      url
      summary
      content
      createdAt
    }
  }
`;

export {GET_HISTORY_SUMMARY, GET_RECENT_SUMMARYS};
