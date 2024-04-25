FROM mcr.microsoft.com/mssql/server:2019-latest

COPY init.sql /usr/src/app/
WORKDIR /usr/src/app

# 确保 SQL Server 服务在执行初始化脚本后继续运行
CMD /bin/bash -c "/opt/mssql/bin/sqlservr & (sleep 30; /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'p@ssw0rd123' -i init.sql) & wait"
