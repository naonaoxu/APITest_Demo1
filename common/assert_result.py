from common.log import MyLog

log= MyLog()

class AssertResult:

    @classmethod
    def assert_code(self,result_code,expected_code):
        """验证response状态码"""
        try:
            assert result_code == expected_code
            log.info("success assert status code")
            return True
        except :
            log.error("faile asssert status code")


    def assert_body(self,body,body_msg,expected_msg):
        """验证response body中任意属性的值"""
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            log.error("faile asssert body")


    def assert_msg_in_text(self,acture_msg,expect_msg):
        """验证response body中是否包含预期字符串"""
        try:
            assert expect_msg in acture_msg
            return True
        except:
            log.error("faile asssert in text")

    def assert_text(self,body,expect_msg):
        """验证response body中是否等于预期字符串"""
        try:
            assert body == expect_msg
            return True
        except:
            log.error("faile asssert text")






