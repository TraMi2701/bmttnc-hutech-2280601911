from SinhVien import SinhVien
# class SinhVien:
class QuanLySinhVien:
    def __init__(self): 
        self.listSinhVien = [] 

    def generateID(self):
        maxId = 1
        if len(self.listSinhVien) > 0:
            maxId = max(sv._id for sv in self.listSinhVien) + 1  
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svid = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        try:
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv = SinhVien(svid, name, sex, major, diemTB)
            self.xepLoaiHocLuc(sv)
            self.listSinhVien.append(sv)
            print(f"Them sinh vien voi ID = {svid} thanh cong!")
        except ValueError:
            print("Loi: Vui long nhap diem la so hop le!")

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            try:
                diemTB = float(input("Nhap diem cua sinh vien: "))
                sv._name = name
                sv._sex = sex
                sv._major = major
                sv._diemTB = diemTB
                self.xepLoaiHocLuc(sv)
            except ValueError:
                print("Loi: Vui long nhap diem la so hop le!")
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._id == ID:
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}"
              .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien