from typing import Optional


class Email:
    def __init__(
        self,
        from_email: dict,
        to: list[dict],
        subject: str,
        text: Optional[str] = None,
        html: Optional[str] = None,
        template: Optional[str] = None,
        template_vars: Optional[dict] = None,
        cc: Optional[list[dict]] = None,
        bcc: Optional[list[dict]] = None,
    ) -> None:
        self.from_email = from_email
        self.to = to
        self.subject = subject
        self.text = text
        self.html = html
        self.template = template
        self.template_vars = template_vars
        self.cc = cc
        self.bcc = bcc

    def get(self) -> dict:
        return {
            "from": self.from_email,
            "to": self.to,
            "subject": self.subject,
            "text": self.text,
            "html": self.html,
            "template": self.template,
            "template-vars": self.template_vars or {},
            "cc": self.cc or [],
            "bcc": self.bcc or [],
        }
