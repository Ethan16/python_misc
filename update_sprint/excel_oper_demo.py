# -*- coding: utf-8 -*-
import json
import re
import xlrd
import copy

from xlwt import *
from xlutils import copy as xlutils_copy


class ReadExcel(object):
    def __init__(self, excel_file_path=None, by_index=None, by_name=None):
        """
        :param excel_file_path: The excel file path
        :param by_index: Index of the sheet required
        :param by_name: Name of the sheet required
        """
        self.excel_file = excel_file_path
        self.sheet = self._open_excel(by_index=by_index, by_name=by_name)

    def _open_excel(self, by_index=None, by_name=u'Sheet1'):
        """
        Open a spreadsheet file for data extraction.
        :param by_index: Index of the sheet required
        :param by_name: Name of the sheet required
        :return: One of the excel sheet
        """
        workbook = xlrd.open_workbook(filename=self.excel_file, formatting_info=True)
	sheets = workbook.sheets()
	for sheet in sheets:
	    if by_name in str(sheet.name):
		return sheet
	    else:
		for s in by_name.split("~"):
		    if s in str(sheet.name):
			return sheet
        #if by_index is not None:
        #    sheet = workbook.sheet_by_index(by_index)
        #else:
        #    sheet = workbook.sheet_by_name(by_name)
        #return sheet

    def _get_merged_cells_position(self, all_data=None):
        """
        To add the content of the merged cells
        :param all_data: All of the data in the sheet, but does't include the merged cells
        :return: All of the data in the sheet, and include the merged cells
        """
        merged_cells = self.sheet.merged_cells
        multiple_group_merged = []  # the location of multiple sets of merged cells [merge1, merge2, merge3...]
        for merged_cell_index in range(0, len(merged_cells)):
            merged_cell = merged_cells[merged_cell_index]
            row_diff = merged_cell[1] - merged_cell[0]
            col_diff = merged_cell[3] - merged_cell[2]
            a_group_merged = []  # the location of a group of merged cells,[[row1, col1], [row2, col2]...]
            if row_diff is not 1:
                for i in range(merged_cell[0], row_diff + merged_cell[0]):
                    a_group_merged.append([i, merged_cell[2]])
            else:
                for i in range(merged_cell[2], col_diff + merged_cell[2]):
                    a_group_merged.append([merged_cell[0], i])

            multiple_group_merged.append(a_group_merged)

        for row_index, row_data in all_data.items():
            for col_index in range(0, len(row_data)):
                if all_data[row_index][col_index] in ['', u'']:
                    for a_group_merged in multiple_group_merged:
                        if [row_index, col_index] in a_group_merged:
                            # the row and col is the first location of the merged cells
                            row = a_group_merged[0][0]
                            col = a_group_merged[0][1]
                            all_data[row_index][col_index] = all_data[row][col]
        return all_data

    def get_all_excel_data_by_row(self):
        """
        Obtain data from Excel tables based on the index or name of the sheet
        :return: The dict type data of excel table by row
        """
        nrows = self.sheet.nrows  # number of rows
        all_data = {}
        for row_num in range(0, nrows):
            row_data = self.sheet.row_values(row_num)  # A row of data
            for col_num in range(0, len(row_data)):
                if type(row_data[col_num]) is not unicode:
                    row_data[col_num] = unicode(row_data[col_num])
            all_data.update({row_num: row_data})
        ret = self._get_merged_cells_position(all_data=all_data)
        return all_data

    def get_all_excel_data_by_col(self):
        """
        Obtain data from Excel tables based on the index or name of the sheet
        :return: The dict type data of excel table by column
        """
        ncols = self.sheet.ncols  # number of columns
        all_data = {}
        for col_num in range(0, ncols):
            col_data = self.sheet.col_values(col_num)  # A column of data
            all_data.update({col_num: col_data})
        return all_data

    def get_data_by_specify_row_col(self, row=0, col=0):
        """
        Gets the data by specifying row and column
        :param row: Specifying row
        :param col: Specifying column
        :return:
        """
        all_data = self.get_all_excel_data_by_row()
        return all_data[row][col]

    def dict_to_json(self, dict_datas=None):
        """
        Convert dict to json
        :param dict_datas: Data to be converted
        :return: Json data
        """
        json_datas = {}
        for index, data in dict_datas.items():
            json_datas[str(index)] = json.JSONEncoder().encode(data)
        json_datas = json.JSONEncoder().encode(json_datas)
        return json_datas

    def json_to_dict(self, json_datas=None):
        """
        Convert json to dict
        :param json_datas: Data to be convert
        :return: Dict data
        """
        dict_datas = {}
        for key, value in json.loads(json_datas).items():
            # 1. Remove these characters: []"
            # 2. Replace character \ with \\
            value = json.loads(' "%s" ' % (re.sub('[]["]', '', value)))
            # Convert the string to list
            list_value = [x for x in (value).split(',')]
            # Remove the leading space
            for i in range(0, len(list_value)):
                list_value[i] = list_value[i].lstrip()
            dict_datas[int(key)] = list_value
        return dict_datas


class WriteExcel(object):
    def _creak_excel(self):
        return Workbook(encoding='ascii')

    def _creak_sheet(self, excel=None, sheet_name='Sheet1'):
        return excel.add_sheet(sheet_name)

    def write_sheet(self, work_sheet=None, data=None, row=0, col=0):
        work_sheet.write(row, col, label=data)

    def save_excel(self, excel=None, excel_name='My_excel.xls'):
        excel.save(excel_name)

    def write_data_to_new_file(self, dict_datas=None, sheet_name='Sheet1', excel_name='My_excel.xls'):
        excel = self._creak_excel()
        work_sheet = self._creak_sheet(excel, sheet_name)
        for row, value in dict_datas.items():
            for col in range(len(value)):
                try:
                    value[col] = float(value[col])
                    self.write_sheet(work_sheet, value[col], row, col)
                except ValueError:
                    self.write_sheet(work_sheet, value[col], row, col)
        self.save_excel(excel, excel_name)


class UpdateExcel(object):
    def __init__(self, desti_file=None):
        self.excel = xlrd.open_workbook(filename=desti_file, formatting_info=True)
        self.sheet = None
        self.excel_copy = xlutils_copy.copy(self.excel)
        self.people_time = {}
        self.style = XFStyle

    def copy_sheet(self, excel, source_index, new_name):
        """
         Copy one sheet
        :param excel: Excel of the copied sheet
        :param source_sheet: The copied sheet
        :param new_name: The new name of the sheet by copying generated
        :return: A :class:`~xlrd.sheet.Sheet`.
        """
        sheets = excel._Workbook__worksheets
        for sheet in sheets:
            if sheet.name == new_name:
                return sheet
        new_sheet = copy.deepcopy(excel.get_sheet(source_index))
        sheets.append(new_sheet)
        append_index = len(excel._Workbook__worksheets) - 1
        excel.set_active_sheet(append_index)
        excel.get_sheet(append_index).set_name(new_name)
        return excel.get_sheet(append_index)

    def update_excel_file(self, excel_file_path=None, dict_datas=None, by_index=1):
        excel = xlrd.open_workbook(filename=excel_file_path, formatting_info=True)
        excel_copy = copy.copy(excel)
        sheet = excel_copy.get_sheet(by_index)
        for row, value in dict_datas.items():
            for col in range(len(value)):
                try:
                    value[col] = float(value[col])
                    self.set_out_cell(sheet, col, row, value[col])
                except ValueError:
                    self.set_out_cell(sheet, col, row, value[col])

        excel_copy.save(excel_file_path)

    def update_excel(self, source_files=None, desti_file=None, new_sheet_name=None, by_name=None, is_style=False,
                     data_rows=50):
        """
        Update multiple files to destination file
        :param source_files: Source file, type: list
        :param desti_file: destination file, type: string
        :param dict_datas: The data to be updated, type: dict
        :param by_index: Index of the sheet required
        :return:
        """
	desti_excel_copy = self.excel_copy
        desti_sheet = self.copy_sheet(desti_excel_copy, u'sprint-模板', new_sheet_name)
        all_datas = {}
        all_datas_key = 3
        serial_number = 1
	self.people_time = {}
        for s_file in source_files:
            try:
                read_excel = ReadExcel(excel_file_path=s_file, by_name=by_name)
            except xlrd.biffh.XLRDError as e:
                continue
            sheet = read_excel.sheet
	    if sheet is None:
		continue
            person = sheet.cell(3, 3).value
            if person == '':
                continue
            remaining_time = 0
            total_time = 0
            nrows = sheet.nrows
            for row_num in range(3, nrows):
		if unicode(sheet.cell(row_num, 4).value) != u'N/A':
		    try:
		        remaining_time = remaining_time + float(sheet.cell(row_num, 12).value)
                    except ValueError as e:
		        if sheet.cell(row_num, 12).value is (u'' or ''):
			   pass
		        else:
			   raise e
		    try:
                        total_time = total_time + sheet.cell(row_num, 5).value
                    except TypeError as e:
                        if sheet.cell(row_num, 5).value is (u'' or ''):
                           pass
                        else:
                           raise e
                break_flag = 0
                row_data = sheet.row_values(row_num)  # A row of data
                for col_num in range(0, len(row_data)):
                    if col_num == 0:
                        row_data[col_num] = serial_number
                        serial_number = serial_number + 1
                    if type(row_data[col_num]) is not unicode:
                        row_data[col_num] = unicode(row_data[col_num])
                    if col_num == 2 and row_data[col_num] == (u'' or ''):
                        break_flag = 1
                        serial_number = serial_number - 1
                if break_flag == 1:
                    break
                all_datas.update({all_datas_key: row_data})
                all_datas_key = all_datas_key + 1
            self.people_time[person] = {"remaining_time": remaining_time,
                                        "total_time": total_time,
                                        "over_time": total_time - remaining_time}

        for row, value in all_datas.items():
            for col in range(len(value)):
                try:
                    value[col] = float(value[col])
                    self.set_out_cell(desti_sheet, col, row, value[col])
                except ValueError:
                    self.set_out_cell(desti_sheet, col, row, value[col])

        desti_excel_copy.save(desti_file)
        self.excel = xlrd.open_workbook(filename=desti_file, formatting_info=True)
        self.sheet = self.excel.sheet_by_name(new_sheet_name)
        style = self.set_style(self.fnt_style(), self.borders_style(), self.alignment_style())
        for col in range(6, 13):
            col_value = self.calculate_day_time(self.sheet, col)
            if is_style:
                desti_sheet.write(2, col, col_value, style)
            else:
                desti_sheet.write(2, col, col_value)
        if is_style:
            self.calculate_person_time(desti_sheet, style, row=data_rows)
        else:
            self.calculate_person_time(desti_sheet, row=data_rows)
        desti_excel_copy.save(desti_file)

        # 解决某同事去除某项任务后合并的表还存在
        self.excel = xlrd.open_workbook(filename=desti_file, formatting_info=True)
        self.sheet = self.excel.sheet_by_name(new_sheet_name)
        real_rows = 0
        empty_row_data = []
        empty_datas = {}
        for row in range(3, data_rows):
            row_data = self.sheet.row_values(row)
            if row_data[1] == ('' or u''):
                break
            else:
                real_rows = real_rows + 1
        empty_row_data = self.sheet.row_values(real_rows + 3)
        all_data_rows = len(all_datas)
        if all_data_rows < real_rows:
            for row in range(all_data_rows, real_rows):
                empty_datas.update({all_datas_key: empty_row_data})
                all_datas_key = all_datas_key + 1
        for row, value in empty_datas.items():
            for col in range(len(value)):
                if col == 0:
                    value[col] = serial_number
                    serial_number = serial_number + 1
                try:
                    value[col] = float(value[col])
                    self.set_out_cell(desti_sheet, col, row, value[col])
                except ValueError:
                    self.set_out_cell(desti_sheet, col, row, value[col])
        desti_excel_copy.save(desti_file)

    def _get_out_cell(self, sheet, col_index, row_index):
        """ HACK: Extract the internal xlwt cell representation. """
        row = sheet._Worksheet__rows.get(row_index)
        if not row:
            return None
        cell = row._Row__cells.get(col_index)
        return cell

    def set_out_cell(self, sheet, col, row, value):
        """ Change cell value without changing formatting. """
        # HACK to retain cell style.
        previous_cell = self._get_out_cell(sheet, col, row)
        # END HACK, PART I
        sheet.write(row, col, value)
        # HACK, PART II
        if previous_cell:
            new_cell = self._get_out_cell(sheet, col, row)
            if new_cell:
                new_cell.xf_idx = previous_cell.xf_idx

    def calculate_cell_value(self, sheet, from_cell_range, col_row='col'):
        """

        :param sheet:
        :param cell:
        :param from_cell_range: dict
        :param col_row:
        :return:
        """
        nrows = sheet.nrows  # number of nrows
        ncols = sheet.ncols  # number of columns
        ret_value = 0
        if col_row == 'col':
            for col_num in range(0, ncols):
                col_data = sheet.col_values(col_num)  # A column of data
                if col_num == from_cell_range["cell"]:
                    for row_num in range(from_cell_range["start"], from_cell_range["end"]):
                        ret_value = ret_value + float(str(col_data[row_num]))

        else:
            for row_num in range(0, nrows):
                row_data = sheet.row_values(row_num)
                if row_num == from_cell_range["cell"]:
                    for col_num in range(from_cell_range["start"], from_cell_range["end"]):
                        ret_value = ret_value + float(str(row_data[col_num]))

        return ret_value

    def calculate_day_time(self, sheet, col):
        from_range = {}
        nrows = sheet.nrows
        ncols = sheet.ncols
        for row_num in range(3, nrows):
            col_data = sheet.col_values(col)
            if col_data[row_num] == (u'' or ''):
                from_range["end"] = row_num - 12
                break
        from_range["start"] = 3
        from_range["cell"] = col
        return self.calculate_cell_value(sheet, from_range)

    def calculate_person_time(self, sheet, style=None, row=50):
        t_total_time = 0
        t_remaining_time = 0
        t_over_time = 0
        if style is None:
            style = Style.default_style
        for key, value in self.people_time.items():
            sheet.write(row, 1, key, style=style)
            sheet.write(row, 2, value['total_time'], style=style)
            sheet.write(row, 3, value['remaining_time'], style=style)
            sheet.write(row, 4, value['over_time'], style=style)
            if value['total_time'] == 0:
                sheet.write(row, 5, "#DIV/0/!", style=style)
            else:
                sheet.write(row, 5, ("%.f%%" % ((value['over_time'] / value['total_time'])*100)), style=style)
            t_total_time = t_total_time + value['total_time']
            t_remaining_time = t_remaining_time + value['remaining_time']
            t_over_time = t_over_time + value['over_time']
            row = row + 1
	#last_row = row + 1
        last_row = row
        sheet.write(last_row, 1, u'汇总', style=style)
        sheet.write(last_row, 2, t_total_time, style=style)
        sheet.write(last_row, 3, t_remaining_time, style=style)
        sheet.write(last_row, 4, t_over_time, style=style)
        if t_total_time == 0:
            sheet.write(last_row, 5, "#DIV/0/!", style=style)
        else:
            sheet.write(last_row, 5, ("%.f%%" % ((t_over_time / t_total_time)*100)), style=style)

    def fnt_style(self, name=u'宋体'):
        fnt = Font()
        fnt.name = name
        return fnt

    def borders_style(self):
        borders = Borders()
        borders.top = borders.THIN
        borders.left = borders.THIN
        borders.bottom = borders.THIN
        borders.right = borders.THIN
        return borders

    def alignment_style(self):
        alignment = Alignment()
        alignment.horz = alignment.HORZ_CENTER
        return alignment

    def set_style(self, fnt, borders, alignment):
        style = XFStyle()
        style.font = fnt
        style.borders = borders
        style.alignment = alignment
        return style


if __name__ == "__main__":
    # test = ReadExcel(u'aCMP5.8.1-测试SprintBacklog.xls', 1)
    # # test = ReadExcelDemo(u'test.xls', 0)
    # row_datas = test.get_all_excel_data_by_row()
    # json_datas = test.dict_to_json(row_datas)
    # print "row_datas = %s" % row_datas
    # print "json_datas = %s" % json_datas
    # # Analytic JSON to dict
    # dict_datas = test.json_to_dict(json_datas)
    # print "dict_datas = %s" % dict_datas
    # print dict_datas == row_datas
    #
    # test_write = WriteExcel()
    # test_write.write_data_to_new_file(dict_datas)
    test_update = UpdateExcel(u'aCloud5.8.5-测试SprintBacklog.xls')

    test_update.update_excel([u'aCloud5.8.5-测试SprintBacklog - fengyuan.xls',
                              u'aCloud5.8.5-测试SprintBacklog - rsy.xls',
                              u'aCloud5.8.5-测试SprintBacklog - cwx.xls',
                              u'aCloud5.8.5-测试SprintBacklog - czc.xls',
                              u'aCloud5.8.5-测试SprintBacklog - hwc.xls',
                              u'aCloud5.8.5-测试SprintBacklog - liulei.xls',
                              u'aCloud5.8.5-测试SprintBacklog - liutao.xls',
                              u'aCloud5.8.5-测试SprintBacklog - zyc.xls',
                              ],
                             u'aCloud5.8.5-测试SprintBacklog.xls', u'sprint-（10.23~10.27)', u'sprint-模板 （10.23~10.27)')

    test_update = UpdateExcel(u'aCloud5.8.5-测试SprintBacklog.xls')
    test_update.update_excel([u'aCloud5.8.5-测试SprintBacklog - fengyuan.xls',
                              u'aCloud5.8.5-测试SprintBacklog - rsy.xls',
                              u'aCloud5.8.5-测试SprintBacklog - cwx.xls',
                              u'aCloud5.8.5-测试SprintBacklog - czc.xls',
                              u'aCloud5.8.5-测试SprintBacklog - hwc.xls',
                              u'aCloud5.8.5-测试SprintBacklog - liulei.xls',
                              u'aCloud5.8.5-测试SprintBacklog - liutao.xls',
                              u'aCloud5.8.5-测试SprintBacklog - zyc.xls',
                              ],
                             u'aCloud5.8.5-测试SprintBacklog.xls', u'sprint-（10.23~10.27)',
                             u'sprint-模板 （10.23~10.27)', True)
    test_update.update_excel([u'aCloud5.8.5-测试SprintBacklog - fengyuan.xls',
                              u'aCloud5.8.5-测试SprintBacklog - rsy.xls',
                              u'aCloud5.8.5-测试SprintBacklog - cwx.xls',
                              u'aCloud5.8.5-测试SprintBacklog - czc.xls',
                              u'aCloud5.8.5-测试SprintBacklog - hwc.xls',
                              u'aCloud5.8.5-测试SprintBacklog - liulei.xls',
                              u'aCloud5.8.5-测试SprintBacklog - liutao.xls',
                              u'aCloud5.8.5-测试SprintBacklog - zyc.xls',
                              ],
                             u'aCloud5.8.5-测试SprintBacklog.xls', u'sprint-（10.30~11.3)',
                             u'sprint-模板 （10.30~11.3)', True)
