import { Card, CardContent, CardMedia, Grid } from '@mui/material';
import React from 'react'

const SinglePost = ({postData}) => {
  return (
    <Card sx={{maxWidth: 345}}>
      <CardMedia
        component="img"
        height="150"
        image="https://mui.com/static/images/cards/contemplative-reptile.jpg"
        alt='green iguana'
      />
      <CardContent>
        <h3>{postData.title.substr(0, 20)}...</h3>
        <p>{postData.content.substr(0, 50)}...</p>
      </CardContent>
    </Card>
  );
}


const Posts = ({postsData}) => {
  console.log(postsData);

  return (
    <Grid container spacing={2} style={{padding: "0 1em"}}>
      {
        postsData?.map(post => {
          return (
            <Grid key={post.id} item xs={4}>
              <SinglePost postData={post}/>
            </Grid>
          );
        })
      }
    </Grid>
  );
}

export default Posts