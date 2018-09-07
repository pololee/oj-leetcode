import collections


class PrintEdges:
    def edges(self, lines):
        """
        :type lines: list[str]
        :rtype list[str]
        """
        edges = []
        table = collections.defaultdict(list)

        for line in lines:
            edges_on_line = self.edges_on_the_line_less_space(line)
            if edges_on_line:
                edges.append(edges_on_line)
            self.build_col_table(line, table)
        
        for _, stack in table.items():
            edges_in_stack = self.edges_in_stack(stack)
            if edges_in_stack:
                edges.append(edges_in_stack)

        return edges


    def build_col_table(self, line, table):
        for idx, ch in enumerate(line):
            if ch.isalpha():
                table[idx].append(ch)
            elif ch == " ":
                table[idx].append("#")
    
    def edges_in_stack(self, stack):
        edges = []
        while stack:
            ch = stack.pop()
            if ch.isalpha() and stack and stack[-1].isalpha():
                edges.append(stack[-1] + ch)
        return edges

    def edges_on_the_line_less_space(self, line):
        edges = []
        stack = []

        for ch in line:
            if ch.isalpha():
                if not stack:
                    stack.append(ch)
                else:
                    other_ch = stack.pop()
                    edges.append(other_ch + ch)
                    stack.append(ch)
        return edges

    def edges_on_the_line(self, line):
        edges = []
        stack = []
        for ch in line:
            if ch.isalpha():
                stack.append(ch)
            elif ch == " ":
                stack.append("#")

        while stack:
            ch = stack.pop()
            if ch.isalpha() and stack and stack[-1].isalpha():
                edges.append(stack[-1] + ch)

        return edges


def main():
    printer = PrintEdges()
    # print(printer.edges_on_the_line("A---B---C"))
    lines = [
    'A----B---C',
    '     |    ',
    '     |    ',
    '     D    '
    ]
    lines = [
        'A',
        '|',
        '|',
        '|',
        'B',
        '|',
        '|',
        '|',
        'C'
    ]
    print(printer.edges(lines))


if __name__ == '__main__':
    main()
