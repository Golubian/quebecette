from testers.cpiscine.CommonTester import CommonTester
from utils.ExecutionContext import TestRunInfo


class C06Tester(CommonTester):

	name = "c06"

	def __init__(self, info: TestRunInfo):
		super().__init__(info)

	def ex00(self):
		self.is_program = True
		self.exercise_files = ["ft_print_program_name.c"]
		self.test_files = []
		self.custom_program_name = "IChangedMyProgramName.out"
		self.program_args = ["Hello", "World!"]
		self.compile_flags = ["-Wextra", "-Werror", "-Wall", "-o", "IChangedMyProgramName.out"]

	def ex01(self):
		self.is_program = True
		self.exercise_files = ["ft_print_params.c"]
		self.test_files = []
		self.program_args = ["Hello", "World!", "Ouais Mec C<est C00l"]
		self.compile_flags = ["-Wextra", "-Werror", "-Wall"]

	def ex02(self):
		self.is_program = True
		self.exercise_files = ["ft_rev_params.c"]
		self.test_files = []
		self.program_args = ["Le gars du monopoly", "son chapeau", "est long et noir"]
		self.compile_flags = ["-Wextra", "-Werror", "-Wall"]
	
	def ex03(self):
		self.is_program = True
		self.exercise_files = ["ft_sort_params.c"]
		self.test_files = []
		self.program_args = ["Alloha!", "World!", "z", "0100" "10", "10", "1", "0 0"]
		self.compile_flags = ["-Wextra", "-Werror", "-Wall"]