import streamlit.web.bootstrap as bootstrap
import streamlit

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

streamlit._is_running_with_streamlit = True
bootstrap.run('web可视化数据.py', 'streamlit run', (), {})


