
import secrets

secret_key = "854ea1961c38c22e3765ae19ff9530e2"
# secret_key = secrets.token_hex(16) // to genrate secret_key

oracle, postgress, mysql= 'oracle','postgress','mysql'
SQL_URI={
    oracle: 'oracle://hr:hr@localhost:1521/xe',
    # postgress: 'postgresql://postgres:root@localhost/RTM_DB',
    postgress: 'postgresql://jdhnqbriwmirpq:5939355f63dc41632b9f5ff907a9e6db6f67bf9e6278bbf04df78600f230eb52@ec2-44-208-88-195.compute-1.amazonaws.com:5432/deq22c1ut0lokj',
    mysql: 'mysql://root:root@localhost/day16'
}
mongodb='mogodb'
NOSQL_URI= {
    mongodb:'mongodb+srv://user1:HiwaW0Jo4eBNeJTD@cluster0.sydu8iv.mongodb.net/test'
    # mongodb:'mongodb://localhost:27017/'
}
table_base_URL="/"
base_file_path="/"