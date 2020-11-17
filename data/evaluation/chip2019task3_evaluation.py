#! python3
# *_* coding: utf-8 *_*

"""CHIP 2019 Task 3 Evaluation Script."""


import os
import sys
import codecs
from collections import defaultdict

class Metrics(object):
    """define evaluation metrics."""
    def __init__(self, tp=0, tn=0, fp=0, fn=0):
        """initialization"""
        assert type(tp) == int
        assert type(tn) == int
        assert type(fp) == int
        assert type(fn) == int
        self.tp = tp
        self.tn = tn
        self.fp = fp
        self.fn = fn

    def precision(self):
        """caculate precision score."""
        try:
            return self.tp / (self.tp + self.fp)
        except ZeroDivisionError:
            return 0.0

    def recall(self):
        """caculate recall score."""
        try:
            return self.tp / (self.tp + self.fn)
        except ZeroDivisionError:
            return 0.0

    def f1(self):
        """caculate f1 score (beta=1)."""
        try:
            return (2 * self.precision() * self.recall()) / (self.precision() + self.recall())
        except ZeroDivisionError:
            return 0.0


class Record_results(object):
    """scan the input file, record tp, tn, fp, fn for evaluate."""
    def __init__(self, gold_file, system_file):

        with codecs.open(gold_file, "r", encoding="utf-8") as f2:
            self.gold_results = {line.strip().split("\t")[0]:line.strip().split("\t")[1] for line in f2}

        with codecs.open(system_file, "r", encoding="utf-8") as f1:
            self.system_results = {line.strip().split("\t")[0]:line.strip().split("\t")[1] for line in f1}

        self.processed_sentences = list(set(self.gold_results.keys()) | set(self.system_results.keys()))

        self.tags = ('Addictive Behavior', 'Address', 'Age', 'Alcohol Consumer', 'Allergy Intolerance', 'Bedtime', 'Blood Donation', 'Capacity', 'Compliance with Protocol', 'Consent', 'Data Accessible', 'Device', 'Diagnostic', 'Diet', 'Disabilities', 'Disease', 'Education', 'Encounter', 'Enrollment in other studies', 'Ethical Audit', 'Ethnicity', 'Exercise', 'Gender', 'Healthy', 'Laboratory Examinations', 'Life Expectancy', 'Literacy', 'Multiple', 'Neoplasm Status', 'Non-Neoplasm Disease Stage', 'Nursing', 'Oral related', 'Organ or Tissue Status', 'Pharmaceutical Substance or Drug', 'Pregnancy-related Activity', 'Receptor Status', 'Researcher Decision', 'Risk Assessment', 'Sexual related', 'Sign', 'Smoking Status', 'Special Patient Characteristic', 'Symptom', 'Therapy or Surgery')
        
        self.records = defaultdict(dict)
        for t in self.tags:
            self.records[t] = {"tp":0, "tn":0, "fp":0, "fn":0}
        self._get_results()

    def _get_results(self):
        for s in self.processed_sentences:
            print(s)
            if self.gold_results[s] == self.system_results[s]:
                self.records[self.gold_results[s]]["tp"] += 1
            if self.gold_results[s] != self.system_results[s]:
                self.records[self.gold_results[s]]["fn"] += 1
                self.records[self.system_results[s]]["fp"] += 1
        # print(self.records)
        return self.records

class Evaluation(object):
    """run the evaluation."""
    def __init__(self, records):
        self.tags = records.keys()
        self.evaluation = defaultdict(dict)
        for t in self.tags:
            self.evaluation[t] = {"precision":0.0, "recall":0.0, "f1":0.0}

        self.caculate(records)
        self.show_results()

    def caculate(self, records):
        """caculate evaluation results."""
        all_tp, all_tn, all_fp, all_fn = 0, 0, 0, 0
        all_precision, all_recall, all_f1 = [], [], []
        for t in self.tags:
            tp, tn, fp, fn = records[t]["tp"], records[t]["tn"], records[t]["fp"], records[t]["fn"]
            all_tp += tp
            all_tn += tn
            all_fp += fp
            all_fn += fn

            metrics = Metrics(tp=tp, tn=tn ,fp=fp, fn=fn)
            self.evaluation[t]["precision"] = metrics.precision()
            self.evaluation[t]["recall"] = metrics.recall()
            self.evaluation[t]["f1"] = metrics.f1()
            all_precision.append(metrics.precision())
            all_recall.append(metrics.recall())
            all_f1.append(metrics.f1())

        all_metrics = Metrics(tp=all_tp, tn=all_tn, fp=all_fp, fn=all_fn)
        self.micro_precision = all_metrics.precision()
        self.micro_recall = all_metrics.recall()
        self.micro_f1 = all_metrics.f1()
        self.macro_precision = sum(all_precision) / len(all_precision)
        self.macro_recall = sum(all_recall) / len(all_recall)
        self.macro_f1 = sum(all_f1) / len(all_f1)
        # print(self.evaluation)
        return self.evaluation

    def show_results(self):
        print('{:*^100}'.format(' CHIP 2019 TASK 3 '))
        print('{:35}    {:15}  {:15}  {:15}'.format('', 'Precision.', 'Recall.', 'f1.'))
        for t in self.tags:
            print('{:>35}    {:<15.4f}  {:<15.4f}  {:<15.4f}'.format(t, self.evaluation[t]["precision"], self.evaluation[t]["recall"], self.evaluation[t]["f1"]))
        print('{:35}    {:-^15}  {:-^15}  {:-^15}'.format('', '', '', ''))
        print('{:>35}    {:<15.4f}  {:<15.4f}  {:<15.6f}'.format("Overall (micro)", self.micro_precision, self.micro_recall, self.micro_f1))
        print('{:>35}    {:<15.4f}  {:<15.4f}  {:<.6f}{:<40}'.format("Overall (macro)", self.macro_precision, self.macro_recall, self.macro_f1, "(final ranking metric)"))

if __name__ == "__main__":
    gold_file = sys.argv[1]
    system_file = sys.argv[2]
    results = Record_results(gold_file, system_file)
    evaluation = Evaluation(results.records)
