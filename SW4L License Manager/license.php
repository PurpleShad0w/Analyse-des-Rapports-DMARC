<?php
    class Database{ 
        private $host = "localhost"; 
        private $db_name = "LICENSE"; 
        private $username = "root"; 
        private $password = "ac6-dmarc-database"; 
        public $conn; 

        public function getConnection(){ $this->conn = null;
            try{
                $this->conn = new PDO("mysql:host=".$this->host.";dbname=".$this->db_name, $this->username, $this->password);
            }catch(PDOException $exception){
                echo "Connection error: ".$exception->getMessage();
            }
            return $this->conn;
        }
    }

    class License{ 
        private $conn;
        private $table_name = "LICENSES";
        public $record;
        public $mac;
        public $email;
        public $type;
        public $feature;
        public $until;
        public $key_;
        public $input_mac;
        public $input_email;
        public $input_key_;

        public function __construct($db){ 
            $this->conn = $db;
        }
        public function getRecord(){
            $query = "SELECT mac, email, type, feature, until, key_ FROM " . $this->table_name . " WHERE record_id = '" . $this->record . "'";

            $stmt = $this->conn->prepare( $query );
            $stmt->execute();

            return $stmt;
        }

        public function getKey(){
            $query = "SELECT key_ FROM " . $this->table_name . " WHERE mac = '" . $this->input_mac . "' AND email = '" . $this->input_email . "'";

            $stmt = $this->conn->prepare( $query );
            $stmt->execute();

            return $stmt;
        }

        public function getDate(){
            $query = "SELECT until FROM " . $this->table_name . " WHERE mac = '" . $this->input_mac . "' AND email = '" . $this->input_email . "'";

            $stmt = $this->conn->prepare( $query );
            $stmt->execute();

            return $stmt;
        }

        public function getMac(){
            $query = "SELECT mac FROM " . $this->table_name . " WHERE key_ = '" . $this->input_key_ . "' AND email = '" . $this->input_email . "'";

            $stmt = $this->conn->prepare( $query );
            $stmt->execute();

            return $stmt;
        }

        public function checkEmail(){
            $query = "SELECT * FROM " . $this->table_name . " WHERE email = '" . $this->input_email . "'";

            $stmt = $this->conn->prepare( $query );
            $stmt->execute();

            return $stmt;
        }

        public function updateMac(){
            $query_1 = "SET SQL_SAFE_UPDATES = 0;";
            $query_2 = "UPDATE " . $this->table_name . " SET mac = REPLACE(mac, '" . $this->mac . "', '" . $this->input_mac . "');";
            $query_3 = "SET SQL_SAFE_UPDATES = 1;";

            $stmt = $this->conn->prepare( $query_1 );
            $stmt->execute();
            $stmt = $this->conn->prepare( $query_2 );
            $stmt->execute();
            $stmt = $this->conn->prepare( $query_3 );
            $stmt->execute();
        }
    }

    $database = new Database(); 
    $db = $database->getConnection();

    $input_mac = "testmac";
    $input_email = "email.com";

    $license = new License($db);
    $stmt = $license->getDate();
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    print_r($result);

?>