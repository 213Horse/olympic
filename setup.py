from setuptools import setup, find_packages

setup(
    name='Open_source_PhapDien_VietNam',  # Tên của dự án
    version='0.1.0',  

    packages=find_packages(),  

    install_requires=[
        # Các thư viện phụ thuộc cần cài đặt
        'Flask==3.0.0',
    ],

    author='Rune_of_champions',
    author_email='nguyenhoangthanhtrung.univ@gmail.com',

    # Mô tả ngắn về dự án
    description='Ứng dụng LLMs trong việc xử lý các văn bản pháp luật.',
    platforms = ["any"],
    license = ['GNU General Public License (GPL)','MIT License'],
    # URL của dự án
    url='https://github.com/thnhtrung/phap_dien',

)
