import socket
import unittest
from unittest.mock import mock_open, patch

class TestPiScript(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='example.com')
    @patch('socket.socket')
    def test_read_domain_from_file(self, mock_socket, mock_open):
        from pi import get_ip_address
        domain_name = open('domain.txt').read().strip()
        self.assertEqual(domain_name, 'example.com')

    @patch('socket.socket')
    def test_socket_connection(self, mock_socket):
        mock_socket.return_value.connect.return_value = None  # Simulate a successful connection
        from pi import domain_name
        self.assertIsNone(mock_socket().connect((domain_name, 33309)))

if __name__ == '__main__':
    unittest.main()
