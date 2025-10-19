
class DbConnection:
    """A simple class to manage database connections."""
    def __init__(self, db_type, db_name, db_user, db_password, db_host, db_port):
        self.db_type = db_type.lower()
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
    
    @staticmethod
    def is_valid_db_type(db_type):
        """_summary_

        Args:
            db_type (_type_): E.g: 'mysql'

        Returns:
            _type_: returns True if it is valid else False
        """
        valid_types = ['mysql', 'postgresql', 'sqlite', 'oracle', 'snowflake','mssql']
        return db_type in valid_types
    
    @classmethod
    def validate_db_connection_parameters(cls, **params):
        """_summary_

        Args:
            params (dict): Contains database connection parameters

        Returns:
            _type_: Returns True if all parameters are valid else False
        """
        if not isinstance(params.get('db_type', None), str):
            return False
        if not isinstance(params.get('db_name', None), str):
            return False
        if not isinstance(params.get('db_user', None), str):
            return False
        if not isinstance(params.get('db_password', None), str):
            return False
        if not isinstance(params.get('db_host', None), str):
            return False
        if not isinstance(params.get('db_port', None), str) or not isinstance(params.get('db_port', None), int):
            return False
        if not cls.is_valid_db_type(params['db_type']):
            return False
        return True
    