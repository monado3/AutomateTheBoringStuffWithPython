import random
from pathlib import Path

"""
ほんとは
class QAndA
を継承して選択式QAndAを作成し
さらに選択式QAndA_statesを作成するべき
"""


class QandA:
    def __init__(self, q_and_a: dict, answer_options_num=None):
        self.q_and_a = q_and_a
        self.questions_num = len(q_and_a)
        self.wrong_answers_num = answer_options_num - 1

    def correct_answer(self, question: str):
        return self.q_and_a[question]

    def wrong_answers(self, correct_ans: str, num: int):
        answers = list(self.q_and_a.values())
        del answers[answers.index(correct_ans)]
        return random.sample(answers, num)

    def create_one_q_and_a(self, question):
        correct_ans = self.correct_answer(question)
        answers_option = [correct_ans] + self.wrong_answers(correct_ans, self.wrong_answers_num)
        random.shuffle(answers_option)
        return answers_option

    def output_one_q_and_a(self, idx: int, question, answers):
        alpha_lis = [chr(ord('a') + i) for i in range(26)]

        string = f'{idx}. What is the capital of {question}\n\n'
        for alpha, answer in zip(alpha_lis, answers):
            string += f'  {alpha}. {answer}\n'
        return string

    def output_one_suggested_ans(self, idx: int, question, answers):
        alpha_lis = [chr(ord('a') + i) for i in range(26)]

        correct_ans = self.correct_answer(question)
        return f'{idx}. {alpha_lis[answers.index(correct_ans)]}({correct_ans})\n'

    def generate_all_shuffle_q_and_a(self):
        questions = list(self.q_and_a.keys())
        random.shuffle(questions)
        q_lis = []
        a_lis = []
        for idx, question in enumerate(questions, 1):
            answers = self.create_one_q_and_a(question)
            q_lis.append(self.output_one_q_and_a(idx, question, answers))
            a_lis.append(self.output_one_suggested_ans(idx, question, answers))
        return q_lis, a_lis


class Header:
    def __init__(self, header: str):
        self.header = header

    def return_header(self):
        return self.header


class Footer:
    def __init__(self, footer: str):
        self.footer = footer

    def return_footer(self):
        return self.footer


class QuizSheet:
    def __init__(self, q_and_a, header, footer, h_and_m_lf_num, m_and_f_lf_num):
        self.header = header
        self.h_and_m_lf_num = h_and_m_lf_num
        self.q_and_a = q_and_a
        self.m_and_f_lf_num = m_and_f_lf_num
        self.footer = footer

    def make_one_question_sheet(self, sheet_idx: int):
        dir = Path(__file__).resolve().parent / 'quiz'
        file_q = dir / f'capitals_quiz{sheet_idx:02}.txt'
        file_a = dir / f'capitals_quiz_answers{sheet_idx:02}.txt'
        with file_q.open('w', encoding='utf-8') as f_q:
            with file_a.open('w', encoding='utf-8') as f_a:
                f_q.write(self.header.return_header())
                f_q.write('\n' * self.h_and_m_lf_num)

                lis_q, lis_a = self.q_and_a.generate_all_shuffle_q_and_a()
                f_q.write('\n\n'.join(lis_q))

                f_q.write('\n' * self.m_and_f_lf_num)
                f_q.write(self.footer.return_footer())

                f_a.write(''.join(lis_a))

    def make_questions_sheet(self, num: int):
        for idx in range(1, num + 1):
            self.make_one_question_sheet(idx)


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

random.seed(0)
q_and_a = QandA(capitals, 4)

h_str = 'Name:\n\nDate:\n\nPeriod:\n\n'
h_str += ' ' * 20
h_str += 'State Capitals Quiz'

header = Header(h_str)
footer = Footer('-' * 50)
quiz_sheet = QuizSheet(q_and_a, header, footer, 4, 2)
quiz_sheet.make_questions_sheet(35)
