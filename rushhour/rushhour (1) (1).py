import sys
import copy
import random

# constants
DEFAULT_BOARD_STR = "  o aa|  o   |xxo   |ppp  q|     q|     q"
CAR = "xx"

class Board():
    """Represents a Rush Hour board"""

    def __init__(self, board_str):
        self.board = []
        self.board_str = board_str
        self.cars = set()
        rows = board_str.split("|")
        self.cols = len(rows[0])
        for row in rows:
            if len(row) != self.cols:
                raise ValueError("All rows in board must have same length!")

            # TODO: what all other cases are errors?
            # For e.g a 'diagonal' car on the board is handled via 
            # some assert statements (find 'assert' in code)
            lst = []
            for ch in row:
                lst.append(ch)
                self.cars.add(ch)

            self.board.append(lst)

        if ' ' in self.cars:
            self.cars.remove(' ')


    def print(self):
        '''
        Print this board
        '''
        boards = [self]
        self.print_boards(boards)


    def print_boards(self, boards):
        '''
        Print a list of boards horizontally
        '''
        if len(boards) == 0:
            return

        # rows of 1 board
        rows = len(boards[0].board)

        # print top line for all boards
        border = " " + "-"*self.cols + " "
        for i in range(len(boards)):
            print(border, end = " ")
        print()

        # print 0th row of all boards, then 1st..etc
        for i in range(rows):
            for b in boards:
                print("|", end="")
                row = b.board[i]
                for ch in row:
                    print(ch, end="")
                print("| ", end="")
            print()

        # print bottom row for all boards
        border = " " + "-"*self.cols + " "
        for i in range(len(boards)):
            print(border, end = " ")
        print()


    def at_goal(self):
        '''
        is this board at goal?
        It is at goal if the car (xx) is touching the right side.
        Return True if this is a goal board, False otherwise
        '''
        for row in self.board:
            line = "".join(row)  # create a string from the row
            if line.endswith(CAR):
                return True
        return False


    def next(self):
        '''
        Find a list of all possible next boards by moving all cars, 
        and return it
        '''

        next_boards = []
        for car in sorted(self.cars):
            next_list = self.next_for_car(car)
            next_boards.extend(next_list)

        return next_boards
        

    def next_for_car(self, car):
        '''
        return a list of boards that we get as a result of moving a car.
        A car is a single character, for e.g, 'a'
        '''
        next_boards = []
        row_num = self.find_horizontal_loc(car)
        if row_num >= 0:
            horz = self.horizontal_moves(car, row_num)
            next_boards.extend(horz)
        else:
            col_num = self.find_vertical_loc(car)
            assert col_num >= 0, "car %s is not vertical or horizontal!" % car
            vertz = self.vertical_moves(car, col_num)
            next_boards.extend(vertz)
        return next_boards


    def find_horizontal_loc(self, car):
        '''
        return the row number in which this car is horizontal;
        or -1 if this car is not horizontal.
        Car is a single letter, for e.g 'a' or 'x' etc
        '''
        for i in range(len(self.board)):
            line = ''.join(self.board[i])
            if line.find(car+car) >= 0:
                # if there are 2 continuos car chars, it is horizontal
                return i
        return -1


    def horizontal_moves(self, car, row_num):
        '''
        Return a list of all horizontal moves of this car.
        Here, the car will be in horizontal orientation on the board in row
        row_num
        '''

        left  = ''.join(self.board[row_num]).find(car)
        right = ''.join(self.board[row_num]).rfind(car)
        car_len = right-left+1

        assert car_len > 1, "A horizontal car must atleast be 2 chars!"

        lefts = []
        j = left-1
        while j >= 0:
            # try to shift left
            if self.board[row_num][j].isalpha():
                # blocked location; stop trying left
                break

            cpy = self.clone()
            # clear original in copy
            for x in range(left, right+1):
                cpy.board[row_num][x] = ' '

            # and write the new car
            for x in range(j, j+car_len):
                cpy.board[row_num][x] = car


            # update board_str in board as well
            s = ""
            for row in cpy.board:
                s = s + "".join(row) + "|"
            cpy.board_str = s[:-1]

            lefts.append(cpy)
            j -= 1

        # similarly try rights
        rights = []
        j = right+1
        while j < self.cols:
            # try to shift right
            if self.board[row_num][j].isalpha():
                # blocked location; stop trying right
                break

            cpy = self.clone()

            # clear original in copy
            for x in range(left, right+1):
                cpy.board[row_num][x] = ' '

            # and write the new car
            for x in range(j, j-car_len, -1):
                cpy.board[row_num][x] = car

            # update board_str in board as well
            s = ""
            for row in cpy.board:
                s = s + "".join(row) + "|"
            cpy.board_str = s[:-1]

            rights.append(cpy)
            j += 1

        lefts.extend(rights)
        return lefts


    def find_vertical_loc(self, car):
        '''
        return the col number in which this car is vertical;
        or -1 if this car is not vertical.
        Car is a single letter, for e.g 'a' or 'x' etc
        '''
        for j in range(self.cols):
            line = ''
            for i in range(len(self.board)):
                line = line + self.board[i][j]

            if line.find(car+car) >= 0:
                # if there are 2 continuos car chars, it is vertica;
                return j
        return -1


    def vertical_moves(self, car, col_num):
        '''
        Return a list of all vertival moves of this car.
        Here, the car will be in vertival orientation on the board in col
        col_num
        '''
        line = ''
        for i in range(len(self.board)):
            line = line + self.board[i][col_num]

        up   = line.find(car)
        down = line.rfind(car)
        car_len = down-up+1

        assert car_len > 1, "A horizontal car must atleast be 2 chars!"

        ups = []
        i = up-1
        while i >= 0:
            # try to shift up
            if self.board[i][col_num].isalpha():
                # blocked location; stop trying up
                break

            cpy = self.clone()
            # clear original in copy
            for x in range(up, down+1):
                cpy.board[x][col_num] = ' '

            # and write the new car
            for x in range(i, i+car_len):
                cpy.board[x][col_num] = car

            # update board_str in board as well
            s = ""
            for row in cpy.board:
                s = s + "".join(row) + "|"
            cpy.board_str = s[:-1]

            ups.append(cpy)
            i -= 1

        # similarly try downs
        downs = []
        i = down+1
        while i < len(self.board):
            # try to shift down
            if self.board[i][col_num].isalpha():
                # blocked location; stop trying down
                break

            cpy = self.clone()

            # clear original in cpy
            for x in range(up, down+1):
                cpy.board[x][col_num] = ' '

            # and write the new car
            for x in range(i, i-car_len, -1):
                cpy.board[x][col_num] = car

            # update board_str in board as well
            s = ""
            for row in cpy.board:
                s = s + "".join(row) + "|"
            cpy.board_str = s[:-1]

            downs.append(cpy)
            i += 1

        return ups


    def clone(self):
        '''
        return a copy of this board
        '''
        return Board(self.board_str)


    def random_walk(self, N=10):
        '''
        perform a random walk for a maximum of N steps
        '''
        path = Path()
        path.add(self)
        for i in range(N-1):
            current = path.last()
            if current.at_goal():
                break
            children  = current.next()
            rand_next = random.choice(children)  # choose a random choice
            path.add(rand_next)

        return path


    def bfs(self):
        '''
        TODO fixme
        perform a bfs from this starting board
        '''
        queue = [SearchNode(self, None)]  # bfs uses a FIFO queue
        explored = set()
        paths_examined = 0

        while len(queue) > 0:
            #print(len(queue), len(explored))
            node = queue.pop(0)           # FIFO queue - pop from front

            # print the existing path that we are examining
            node.print_path()
            explored.add(node.state.board_str)
            paths_examined += 1

            # add all children to the queue
            for child_state in node.state.next():
                if not child_state.board_str in explored:
                    if child_state.at_goal():
                        # found a path
                        break
                    queue.append(SearchNode(child_state, node))  # FIFO queue - push to back

        return paths_examined


    def astar(self):
        '''
        TODO fixme - astar uses a heuristic
        '''
        queue = [SearchNode(self, None)]
        explored = set()
        paths_examined = 0

        while len(queue) > 0:
            node = queue.pop(0)

            # print the existing path that we are examining
            node.print_path()
            explored.add(node.state.board_str)
            paths_examined += 1

            # add all children to the queue
            for child_state in node.state.next():
                if not child_state.board_str in explored:
                    if child_state.at_goal():
                        # found a path
                        break
                    queue.append(SearchNode(child_state, node))

        return paths_examined




class SearchNode(object):
    '''
    represents a node in the search
    '''
    def __init__(self, state, parent):
        self.state = state 
        self.parent = parent


    def print_path(self):
        '''
        print path from this node back to the parent in some search path
        '''
        node = self
        path = Path()
        path.add(node.state)
        while node.parent:
            path.add(node.parent.state)
            node = node.parent

        # we have a path from current to start.
        # reverse to get a path from start to current
        path.reverse()
        path.print()




## part 2 continuation ##
class Path(object):
    '''
    Represents a path in a goal search. It is a sequence of boards
    '''
    def __init__(self):
        self.seq = []

    def add(self, board):
        '''
        add a board to this path
        '''
        self.seq.append(board)

    def clone(self):
        ''' return a copy of this path'''
        copy = Path()
        for b in self.seq:
            copy.add(Board(b.board_str))
        return copy

    def last(self):
        '''
        return the last board in this path, None if
        this is an empty path
        '''
        if len(self.seq) > 0:
            return self.seq[-1]
        return None


    def reverse(self):
        '''
        reverse this sequence
        '''
        self.seq.reverse()


    def print(self):
        '''
        TODO print this path: max of 6 boards per line
        '''
        if len(self.seq) == 0:
            return

        copy_seq = self.clone().seq

        while len(copy_seq) > 6:
            # print 6 boards max per line
            t = []
            for i in range(6):
                t.append(copy_seq.pop(0))

            t[0].print_boards(t)

        # print the remaining boards
        copy_seq[0].print_boards(copy_seq)


if __name__ == '__main__':
    """ execution starts here """
    if len(sys.argv) == 1:
        print("No arguments supplied!")
        exit(1)

    cmd = sys.argv[1]
    board_str = DEFAULT_BOARD_STR
    if len(sys.argv) == 3:
        board_str = sys.argv[2]

    board = Board(board_str)

    if cmd == "print":
        board.print()
    elif cmd == "done":
        print(board.at_goal())
    elif cmd == "next":
        next_boards = board.next()
        board.print_boards(next_boards)
    elif cmd == "random":
        # added in part 2
        path = board.random_walk()
        path.print()
    elif cmd == "bfs":
        # added in part 2
        paths_examined = board.bfs()
        print(paths_examined)
    elif cmd == "astar":
        # added in part 2
        paths_examined = board.astar()
        print(paths_examined)


# terminal commands to test
# $ sh run.sh print
# $ sh run.sh print "  ooo |ppp q |xx  qa|rrr qa|b c dd|b c ee"

# $ sh run.sh done
# $ sh run.sh done "  oaa |  o   |  o xx|  pppq|     q|     q"

# $ sh run.sh next
# $ sh run.sh next "  ooo |ppp q |xx  qa|rrr qa|b c dd|b c ee"

##### part 2 terminal commands to test #####
# $ sh run.sh random
# $ sh run.sh random "  oaa |  o   |  o xx|  pppq|     q|     q"
# $ sh run.sh random "  oaa |  o   |  oxx |  pppq|     q|     q"

# $ sh run.sh bfs