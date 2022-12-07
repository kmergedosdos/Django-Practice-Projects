import { Box, Divider, Grid, Typography } from '@mui/material';

const styles = {
  box: {
    padding: "3em"
  },
  gridContainer: {
    padding: "2em"
  },
  footerTitle: {
    fontSize: "1.1rem",
    fontWeight: 'bold'
  },
  copyright: {
    textAlign: 'center',
    fontSize: "0.9rem"
  }
}

const footers = [
  {
    title: "Company",
    description: ['Team', 'History', 'Contact us', 'Locations']
  },
  {
    title: "Features",
    description: [
      'Cool Stuff',
      'Random feature',
      'Team feature',
      'Developer stuff',
      'Another one'
    ]
  },
  {
    title: "Resources",
    description: [
      'Resource',
      'Resource name',
      'Another resource',
      'Final resource'
    ]
  },
  {
    title: "Legal",
    description: [
      'Privacy Policy',
      'Terms of use'
    ]
  }
]


const Footer = () => {
  return (
    <>
      <Box style={styles.box}>
        <Divider />
        <Grid container spacing={2} style={styles.gridContainer}>
          {
            footers.map((footer, i) => {
              return (
                <Grid key={i} item xs={3}>
                  <Typography style={styles.footerTitle}>{footer.title}</Typography>
                  <ul>
                    {
                      footer.description.map((item, i) => {
                        return (
                          <li key={i}>{item}</li>
                        );
                      })
                    }
                  </ul>
                </Grid>
              );
            })
          }
        </Grid>
        <div style={styles.copyright}>
          Copyright © BlogmeUp 2022.
        </div>
      </Box>
    </>
  )
}

export default Footer