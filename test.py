import unittest
from filesystem import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_mkdir(self):
        self.fs.mkdir('test')
        self.assertIn('test', self.fs.current_dir.children)

    def test_cd(self):
        self.fs.mkdir('test')
        self.fs.cd('test')
        self.assertEqual(self.fs.current_dir.name, 'test')

    def test_touch(self):
        self.fs.touch('file.txt')
        self.assertIn('file.txt', self.fs.current_dir.children)

    def test_echo(self):
        self.fs.touch('file.txt')
        self.fs.echo('Hello, world!', 'file.txt')
        self.assertEqual(self.fs.current_dir.children['file.txt'], 'Hello, world!')

    def test_mv(self):
        self.fs.touch('file.txt')
        self.fs.mv('file.txt', 'new_file.txt')
        self.assertIn('new_file.txt', self.fs.current_dir.children)
        self.assertNotIn('file.txt', self.fs.current_dir.children)

    def test_cp(self):
        self.fs.touch('file.txt')
        self.fs.cp('file.txt', 'copy.txt')
        self.assertIn('copy.txt', self.fs.current_dir.children)

    def test_rm(self):
        self.fs.touch('file.txt')
        self.fs.rm('file.txt')
        self.assertNotIn('file.txt', self.fs.current_dir.children)

    def test_grep(self):
        self.fs.touch('file.txt')
        self.fs.echo('Hello, world!', 'file.txt')
        matches = self.fs.grep('world', 'file.txt')
        print(matches)
        self.assertEqual(matches, ['world'])

if __name__ == '__main__':
    unittest.main()
