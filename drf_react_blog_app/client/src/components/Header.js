import {
  // AppBar,
  Toolbar,
  Typography
} from '@mui/material';

const styles = {
  header: {
    backgroundColor: 'white',
    borderBottom: '1px solid rgba(0,0,0,0.1)'
  }
}

const Header = () => {

  return (
    <div className='header' style={styles.header}>
      <Toolbar>
        <Typography variant='h6' color="black" noWrap>
          BlogmeUp
        </Typography>
      </Toolbar>
    </div>
  )
}

export default Header